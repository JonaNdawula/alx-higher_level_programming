#!/usr/bin/python3
"""
Start link class to tble in database
"""
import sys
from sqlalchemy import create_engine, select
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format
        (sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    with engine.connect() as connect:
        cmd = select(State).order_by(State.id.asc())
        states = connect.execute(cmd)
        for st in states:
            print(f"{st.id}: {st.name}")

    engine.dispose()
