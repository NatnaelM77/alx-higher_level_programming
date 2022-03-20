#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3], charset="utf8")
    cursor = conn.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON \
            cities.state_id=states.id WHERE states.name LIKE '{:s}' \
            ORDER BY cities.id".format(args[4],)
    cursor.execute(query)
    query_rows = cursor.fetchall()

    print(', '.join(row[0] for row in query_rows))

    cursor.close()
    conn.close()
