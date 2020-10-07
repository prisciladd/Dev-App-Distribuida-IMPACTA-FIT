import psycopg2

connection = psycopg2.connect(
    host = "dbimpacta.postgresql.dbaas.com.br",
    user = "dbimpacta",
    password = "impacta#2020",
    dbname = "dbimpacta")

cursor = connection.cursor()

cursor.execute("SELECT id_cliente, nome, comentario FROM cliente_priscila")

rows = cursor.fetchmany(2)
"""
rows = cursor.fetchall()

for row in rows:
    print("valores:",row[0], row[1], row[2])
"""
for (id_cliente, nome, comentario) in rows:
    print("valores:", id_cliente, nome, comentario)

cursor.close()

connection.close()