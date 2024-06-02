import datetime
from typing import List, Tuple
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import MySQLConnection
from Classes.Enums.Enums import *

load_dotenv()

connection = None
cursor = None

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=os.getenv("user"),
            password=os.getenv("db_password"),
            database="gym_pythonproject"
        )
        print("Conexión exitosa a la base de datos.")
        return connection

    except mysql.connector.Error as error:
        print("Error al conectarse a la base de datos:", error)
        return None


def get_access(id_member: int()):
    global connection, cursor
    try:
        connection = create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.callproc('get_access', [id_member])
            for result in cursor.stored_results():
                rows = result.fetchall()
                return rows
        else:
            return None
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        if connection is not None:
            connection.close()
            print('Conexión a la base de datos cerrada correctamente')
        if cursor is not None:
            cursor.close()
