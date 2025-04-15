import psycopg2

def obtener_preguntas_db():
    connection = psycopg2.connect(
        host="localhost",
        database="root",
        user="AlemEsv",
        password="123456",
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT description, options, correct_answer FROM questions;")
    registros = cursor.fetchall()
    cursor.close()
    connection.close()
    return registros
