#!/usr/bin/python3
"""
List Relationship
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
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    items = sess.query(State).outerjoin(City).all()
    if items:
        for st in items:
            print(f"{st.id}: {st.name}")
            for ct in st.cities:
                print(f"\t{ct.id}: {ct.name}")
