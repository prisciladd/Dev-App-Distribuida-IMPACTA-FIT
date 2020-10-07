import psycopg2

connection = psycopg2.connect(
    host = "dbimpacta.postgresql.dbaas.com.br",
    user = "dbimpacta",
    password = "impacta#2020",
    dbname = "dbimpacta")


column_names = []

data_rows = []

cursor = connection.cursor()

cursor.execute("SELECT * FROM cliente_priscila")

column_names = [desc[0] for desc in cursor.description]

for row in cursor:
    data_rows.append(row)

print("Nome das colunas: {}\n".format(column_names))
print(data_rows[0])