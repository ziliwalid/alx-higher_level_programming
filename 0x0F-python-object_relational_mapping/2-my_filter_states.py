#!/usr/bin/python3
"""
displays all values of a certain state
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    gets the states from db
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
