import psycopg2

def inserir_cliente(nome, comentario):
    try:
        connection = psycopg2.connect(
            host = "dbimpacta.postgresql.dbaas.com.br",
            user = "dbimpacta",
            password = "impacta#2020",
            dbname = "dbimpacta"
        )
        cursor = connection.cursor()
        sql = "INSERT INTO cliente_priscila(nome, comentario) VALUES (%s, %s)"
        cursor.execute(sql, [nome, comentario])
        connection.commit()
        cursor.close()
        connection.close()
        print("Registro Inserido com sucesso")
    except:
        print("Erro ao inserir")    
        
inserir_cliente("Leandro Santos da Silva","Mozão")