import sqlite3
from read_config import read_db_config
import time

def re_connect():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    return cursor, connection


def write_protocol(type, ID, ISBN, Anzahl, user):
    cursor, conn = re_connect()
    zeit=round(time.time())
    cursor.execute("INSERT INTO protocolaus (type, schuelerID, ISBN, Anzahl, unix, user) VALUES (%s, %s, %s, %s, %s, %s)", (type, ID, ISBN, Anzahl, zeit, user))
    conn.commit()

def write_login(user, erfolgreich, IP):
    cursor, conn = re_connect()
    zeit=round(time.time())
    cursor.execute("INSERT INTO protocollogin (user, unix, erfolgreich, IP) VALUES (%s, %s, %s, %s)", (user, zeit, erfolgreich, IP))
    conn.commit()