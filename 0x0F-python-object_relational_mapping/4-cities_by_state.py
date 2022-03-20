#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3], charset="utf8")
    cursor = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id=states.id ORDER BY cities.id"
    cursor.execute(query)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
