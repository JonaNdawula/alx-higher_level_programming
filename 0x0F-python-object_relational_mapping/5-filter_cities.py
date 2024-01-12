#!/usr/bin/python3
"""
Takes in name of states and lists cities
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_host = "localhost"
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_name = sys.argv[3]
    port = 3306
    name_of_state = sys.argv[4]

    cmd = "SELECT name FROM cities WHERE \
            state_id = (SELECT id FROM states WHERE name LIKE \
            BINARY %s) ORDER BY cities.id ASC"

    parameters = (name_of_state,)
    data_base = MySQLdb.connect(
        host=mysql_host, user=mysql_user, password=mysql_password,
        database=mysql_name, port=port)
    cursor = data_base.cursor()

    cursor.execute(cmd, parameters)
    rws = cursor.fetchall()

    tpl = []
    for rw in rws:
        tpl.extend(rw)

    print(*tpl, sep=", ")

    cursor.close()
    data_base.close()
