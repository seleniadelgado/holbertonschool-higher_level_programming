#!/usr/bin/python3
import MySQLdb
import sys

connect = MySQLdb.connect(
    host='localhost',
    port=3306,
    database=sys.argv[3],
    user=sys.argv[1],
    passwd=sys.argv[2])
cur = connect.cursor()
cur.execute('SELECT * FROM states ORDER BY states.id ASC')
rows = cur.fetchall()
for row in rows:
        print(row)
cur.close()
connect.close()
