# Streaming Analytics
A data analysis project for a fictional streaming platform, aimed at generating insights to support business decisions — such as subscription plan revenue, user distribution by age group, favorite genres, churn rate, and more.

## How to Run
1. Install Python
2. Install and run MongoDB locally
3. Create a .env file in the project root based on .env.example
4. Install the dependencies:

```
pip install -r requirements.txt
```
5. Run the pipeline:
```
python main.py
```
The generated CSV files will be available in the reports/ folder.


## Technologies
|Technology     | Usage |
|---|---|
|Faker	        |Fake data generation |
|PyMongo	    |MongoDB connection |
|python-dotenv  |Secure credential management via environment variables|
|pandas	        |Data manipulation and CSV export |


-------------------------------------------------------------------------------
# Streaming Analytics
Projeto de análise de dados de uma plataforma de streaming fictícia, com o objetivo de gerar insights que possam orientar decisões de negócio — como retorno por plano de assinatura, distribuição de usuários por faixa etária, gêneros favoritos, taxa de cancelamento e muito mais.

## Como rodar
1. Instale o Python
2. Instale e rode o MongoDB localmente
3. Crie um arquivo .env na raiz do projeto seguindo o .env.example
4. Instale as dependências:

```
pip install -r requirements.txt
```
5. Execute o pipeline:
```
python main.py
```
Os CSVs gerados ficam na pasta reports/.


## Tecnologias
|Tecnologia     | Uso |
|---|---|
|Faker	        |Geração de dados fictícios |
|PyMongo	    |Conexão com o MongoDB |
|python-dotenv  |Proteção de credenciais via variáveis de ambiente |
|pandas	        |Manipulação dos dados e exportação para CSV |
