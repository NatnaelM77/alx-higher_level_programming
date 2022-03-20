#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3], charset="utf8")
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{:s}' \
            ORDER BY id ASC".format(args[4])
    cursor.execute(query)
    query_rows = cursor.fetchall()

    for row in query_rows:
        if row[1] == args[4]:
            print(row)

    cursor.close()
    conn.close()
