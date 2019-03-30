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
    cmd = "SELECT cities.name\
    FROM cities INNER JOIN states \
    ON states.id = cities.state_id \
    WHERE states.name = %s \
    ORDER BY cities.id ASC"
    cur.execute(cmd, (state,))
    rows = cur.fetchall()
    citylist = []
    for row in rows:
        citylist.append(row[0])
    print(', '.join(citylist), end="")
    print()
    cur.close()
    connect.close()
