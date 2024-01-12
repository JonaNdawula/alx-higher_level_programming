#!/usr/bin/python3

"""
Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, text, bindparam

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    name_of_state = sys.argv[4]
    with engine.connect() as connect:
        cmd = select(State).where(State.name == name_of_state)
        sts = connect.execute(cmd).first()
        if sts:
            print(sts.id)
        else:
            print("Not found")

    engine.dispose()
