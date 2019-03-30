#!/usr/bin/python3
"""name of the state, lists cities, using database"""
import MySQLdb
import sys

if __name__ == "__main__":

    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        database=sys.argv[3],
        user=sys.argv[1],
        passwd=sys.argv[2])
    state = sys.argv[4]
    cur = connect.cursor()
    cmd = 'SELECT cities.name FROM cities INNER JOIN states\
    ON states.id = cities.state_id WHERE Bynary state.name = %s\
    ORDER BY cities.id'
    cur.execute(cmd, (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connect.close()
