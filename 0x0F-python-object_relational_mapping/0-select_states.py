#!/usr/bin/python3
"""
gets data from database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    gets the states for DB
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
