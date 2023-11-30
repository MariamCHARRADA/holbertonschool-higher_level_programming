#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    """
    A script that lists all states from the database hbtn_0e_0_usa
    """
engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
)

connection = engine.connect()
cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()
