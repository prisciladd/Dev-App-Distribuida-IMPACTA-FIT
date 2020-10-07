import psycopg2
try:
    connection = psycopg2.connect(
        host = "dbimpacta.postgresql.dbaas.com.br",
        user = "dbimpacta",
        password = "impacta#2020",
        dbname = "dbimpacta"
    )
except psycopg2.OperationalError:
    print('O banco de dados não foi encontrado')
else:
    print('O banco de dados conectado')