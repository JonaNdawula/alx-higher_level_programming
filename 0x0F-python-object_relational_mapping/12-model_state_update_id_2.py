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
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    sess = Session()

    update_a_state = sess.query(State).filter_by(id=2).first()

    if update_a_state:
        update_a_state.name = 'New Mexico'
        sess.commit()
    sess.close()
