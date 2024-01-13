#!/usr/bin/python3
"""
lists all the cities
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    does the same stuff as before 
    lists the cities too
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cursor:
        cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
