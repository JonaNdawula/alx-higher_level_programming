#!/usr/bin/python3
"""
states models
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

    cmd = "SELECT * FROM states WHERE name LIKE BINARY %s \
            ORDER BY id ASC"

    parameters = (name_of_state,)

    data_base = MySQLdb.connect(
        host=mysql_host, user=mysql_user, password=mysql_password,
        database=mysql_name, port=port)
    cursor = data_base.cursor()

    cursor.execute(cmd, parameters)
    rws = cursor.fetchall()

    for rw in rws:
        print(rw)

    cursor.close()
    data_base.close()
