#!/usr/bin/python3
"""
gets the same script safe 
from sql injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {'name': argv[4]
        })

        rows = cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
