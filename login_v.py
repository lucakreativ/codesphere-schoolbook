import os
import time
import socket
import struct
import sqlite3
from read_config import read_db_config

def re_connect():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    return cursor, connection

def check_data(user):
    cursor, conn = re_connect()
    try:
        cursor.execute("SELECT outside FROM user WHERE username=?", (user,))
        data=cursor.fetchall()[0][0]
        if data==1:
            return True
        else:
            return False
    
    except:
        return False

def check_ip(check_ip):

    ip="192.168.0.1"
    mask="255.255.0.0"

    check_ip=''.join([bin(int(x)+256)[3:] for x in check_ip.split('.')])
    mask=''.join([bin(int(x)+256)[3:] for x in mask.split('.')])
    ip=''.join([bin(int(x)+256)[3:] for x in ip.split('.')])


    con=True
    i=0
    while con==True and i<len(ip):
        if check_ip[i]!=ip[i]:
            if mask[i]=="1":
                con=False

        i+=1

    return con

def abfragen(ip):
    status=[]
    cursor, conn = re_connect()
    ab=time.time()-60*10
    cursor.execute("SELECT erfolgreich FROM protocollogin WHERE IP=? AND unix>=?", (ip, ab))
    data=cursor.fetchall()[::-1]

    if len(data)>=20:
        data=data[0:20]
        for i in data:
            status.append(i[0])

        if 1 in status:
            return True
        else:
            return False
    else:
        return True
