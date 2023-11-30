#!/usr/bin/python3
"""
script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
        user=argv[1], 
        password=argv[2], 
        db=argv[3]
        host="localhost",
        port=3306,
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
