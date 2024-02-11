import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of spreadsheet.
SAMPLE_SPREADSHEET_ID = "ID"
SAMPLE_RANGE_NAME = "engenharia_de_software!A1:H27"


def main():
    print("Starting the application...")

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        print("Reading the spreadsheet...")

        # Read the spreadsheet
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result["values"]

        print("Calculating student situations...")

        # Function to calculate the situation of each student
        def calculate_situation(grades, absences):

            total_classes = 60
            naf = 0

            average = sum(grades) / len(grades)
            if absences > total_classes * 0.25:
                return "Reprovado por Falta"
            elif average < 5:
                return "Reprovado por Nota"
            elif 5 <= average < 7:
                naf = max(0, 10 - average)
                return "Exame Final", naf
            else:
                return "Aprovado"

        values_to_add = []
        for row in values[3:]:
            grades = list(map(int, row[3:5]))  # Convert grades to list
            absences = int(row[2])
            situation = calculate_situation(grades, absences)
            if situation[0] == "Exame Final":
                values_to_add.append([situation[0], round(situation[1])])  # Round NAF

            else:
                values_to_add.append([situation, 0])  # Not applicable, set NAF to 0

        print("Updating the spreadsheet with calculated results...")

        result = (
            sheet.values()
            .update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range="G4",
                valueInputOption="USER_ENTERED",
                body={"values": values_to_add},
            )
            .execute()
        )
        print("Spreadsheet updated successfully!")

    except HttpError as err:
        print("An error occurred:")
        print(err)


if __name__ == "__main__":
    main()
