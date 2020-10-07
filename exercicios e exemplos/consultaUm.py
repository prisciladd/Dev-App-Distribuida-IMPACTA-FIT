import psycopg2

connection = psycopg2.connect(
    host = "dbimpacta.postgresql.dbaas.com.br",
    user = "dbimpacta",
    password = "impacta#2020",
    dbname = "dbimpacta")

cursor = connection.cursor()

cursor.execute("SELECT id_cliente, nome, comentario FROM cliente_priscila")

row = cursor.fetchone()

print("valores:", row[0], row[1], row[2])

cursor.close()

connection.close()