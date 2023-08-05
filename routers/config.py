import mysql.connector

db_config = {
    "host": "mysql",
    "user": "myuser",
    "password": "user@123",
    "database": "UserTable",
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()