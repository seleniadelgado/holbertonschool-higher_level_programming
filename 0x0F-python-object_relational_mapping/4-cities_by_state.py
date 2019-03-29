#!/usr/bin/python3
"""lists cities by state"""
import MySQLdb
import sys

if __name__ == "__main__":

    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        database=sys.argv[3],
        user=sys.argv[1],
        passwd=sys.argv[2])
    cur = connect.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities, states\
    WHERE cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connect.close()
