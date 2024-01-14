#!/usr/bin/python3
"""
A script that lists all City
objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    items = sess.query(City).outerjoin(State).all()
    if items:
        for ct in items:
            print(f"{ct.id}: {ct.name} -> {ct.state.name}")
