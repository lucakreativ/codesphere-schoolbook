import sqlite3

connection=sqlite3.connect("database.db")
cursor=connection.cursor()


with open("converted.db", "r") as f:
    cursor.executescript(f.read())