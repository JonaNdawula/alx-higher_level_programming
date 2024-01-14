#!/usr/bin/python3
"""
imroove files
"""
import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    createState = State(name='California')
    createCity = City(name='San Francisco', state=createState)
    sess.add_all([createState,  createCity])
    sess.commit()
    sess.close()
