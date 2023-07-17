import sqlite3

connection=sqlite3.connect("database.db")
cursor=connection.cursor()


with open("database.sql", "r") as f:
    cursor.executescript(f.read())