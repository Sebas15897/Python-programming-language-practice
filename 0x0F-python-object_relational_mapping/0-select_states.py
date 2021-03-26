#!/usr/bin/python3
"""Import MySQLdb"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    Script that lists all states from the database hbtn_0e_0_usa
    '''
db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
states = cur.fetchall()
for i in states:
    print(i)
cur.close()
db.close()
