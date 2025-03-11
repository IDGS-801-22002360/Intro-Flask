import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="alumnos",
            user="root",
            password="Taisf0rd."
        )
        if conn.is_connected():
            print("Conexión a MySQL establecida")
            return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print("Conexión a MySQL cerrada")