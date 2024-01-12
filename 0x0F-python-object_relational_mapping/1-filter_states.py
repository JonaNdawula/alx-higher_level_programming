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

    data_base = MySQLdb.connect(
        host=mysql_host, user=mysql_user, password=mysql_password,
        database=mysql_name, port=port)
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rws = cursor.fetchall() 

    for rw in rws:
        print(rw)

    cursor.close()
    data_base.close()
