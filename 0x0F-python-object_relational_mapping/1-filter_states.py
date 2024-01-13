#!/usr/bin/python3
"""
lists all states
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    gets the states from db using a select
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
