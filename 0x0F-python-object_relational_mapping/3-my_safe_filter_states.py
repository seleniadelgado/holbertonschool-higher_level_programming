#!/usr/bin/python3
"""filter states matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":

    connect = MySQLdb.connect(
        host='localhost',
        port=3306,
        database=sys.argv[3],
        user=sys.argv[1],
        passwd=sys.argv[2])
    state = sys.argv[4]
    cur = connect.cursor()
    cmd = "SELECT * FROM states WHERE name = %s"
    cur.execute(cmd, (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connect.close()
