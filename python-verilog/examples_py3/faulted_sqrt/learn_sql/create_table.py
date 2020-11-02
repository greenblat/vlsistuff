#! /usr/bin/env python3
import os,sys,string
import sqlite3
from sqlite3 import Error



 
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_faults_table = """
CREATE TABLE IF NOT EXISTS faults (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  width INTEGER,
  position INTEGER,
  discovered TEXT,
  notdiscovered TEXT
);
"""

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



def main():
    Db = create_connection('faultsBase.sql')
    execute_query(Db,create_faults_table)

    Fname = sys.argv[1]
    File = open(Fname)

    while 1:
        line = File.readline()
        if line=='': return
        wrds = line.split()
        if len(wrds)==0:
            pass
        elif (wrds[0] == 'register'):
            Query = "INSERT INTO faults (name,width,position,discovered,notdiscovered) VALUES ( '%s', %s, %s, 'false', 'false')"%(wrds[1],wrds[    2],wrds[3])
            print(Query)
            execute_query(Db,Query)

            

if __name__ == '__main__': main()
