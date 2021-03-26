#!/usr/bin/python3
"""Import MySQLdb"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Script that lists all states from the database hbtn_0e_0_usa
    """
db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306,
                charset="utf8")
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))
states = cur.fetchall()
for i in states:
    if i[1] == argv[4]:
        print(i)
cur.close()
db.close()
