<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-layout">Layout</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<br>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python
- Google Sheets API

## Como usar?

## É necessário ter o Python <a href="https://www.python.org/downloads/">instalado</a> na sua máquina

1. Instale as Dependências:

- Antes de executar o script, você precisa garantir que todas as dependências estejam instaladas. Você pode fazer isso usando o pip. Abra o terminal ou prompt de comando e navegue até o diretório onde seu script está localizado. Em seguida, execute o seguinte comando:

```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Este comando instalará as dependências necessárias para autenticação e acesso ao Google Sheets.

2. Execute o Script:

- Depois de instalar as dependências, você pode simplesmente executar o script Python. No terminal ou prompt de comando, navegue até o diretório onde o seu script Python está localizado e execute o seguinte comando:

```
python python-sheets.py
```

3. Siga as Instruções do Programa:
   O programa exibirá mensagens conforme especificado no código, permitindo que você acompanhe seu funcionamento.

## 💻 Projeto

1. Autenticação com o Google Sheets:

A aplicação faz uso da API do Google Sheets para acessar e modificar uma planilha hospedada no Google Drive.
O usuário precisa fornecer credenciais de API do Google, que geralmente estão armazenadas em um arquivo credentials.json.

2. Leitura da Planilha:

A aplicação lê os dados de uma planilha específica do Google Sheets, que contém informações sobre alunos, incluindo seus nomes, notas em provas e número de faltas.

3. Cálculo das Situações dos Alunos:

Com base nas notas obtidas pelos alunos em provas e no número de faltas, a aplicação calcula a situação de cada aluno de acordo com as seguintes regras:
Se a média das notas for inferior a 5, o aluno é considerado "Reprovado por Nota".
Se a média das notas estiver entre 5 e 7, o aluno precisa fazer um "Exame Final". Neste caso, a aplicação calcula a nota necessária para passar no exame final.
Se a média das notas for 7 ou superior, o aluno é considerado "Aprovado".
Se o número de faltas ultrapassar 25% do total de aulas, independentemente das notas, o aluno é considerado "Reprovado por Falta".
Atualização da Planilha com os Resultados Calculados:

Após calcular as situações dos alunos, a aplicação atualiza a planilha do Google Sheets com os resultados calculados, incluindo a situação de cada aluno e, se aplicável, a nota necessária para passar no exame final.

4. Logs de Atividades:

Durante o processo, a aplicação exibe mensagens de log para fornecer feedback sobre as etapas sendo executadas, como a leitura da planilha, o cálculo das situações dos alunos e a atualização da planilha com os resultados.
