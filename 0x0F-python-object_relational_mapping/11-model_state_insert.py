#!/usr/bin/python3

"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    with engine.connect() as connect:
        trans = connect.begin()
        cmd = insert(State).values(name="Louisiana")
        connect.execute(cmd)
        cmd = select(State).where(State.name == "Louisiana")
        st = connect.execute(cmd).fetchone()
        if st:
            print(st.id)
        trans.commit()

    engine.dispose()
