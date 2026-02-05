import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="hsmax302",
        database="mental_health_ai"
    )
