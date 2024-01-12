#!/usr/bin/python3
"""
Python file containing class definition of a city
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    sess = Session()
    res = sess.query(City, State).\
        join(State, State.id == City.state_id).all()
    if res:
        for ct, st in res:
            print(f"{st.name}: ({ct.id}) {ct.name}")
    sess.close()
