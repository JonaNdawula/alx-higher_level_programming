#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    sess = Session()
    delete_states = sess.query(State).filter(State.name.like(f'%a%')).all()
    if delete_states:
        for st in delete_states:
            sess.delete(st)
        sess.commit()

    sess.close()
