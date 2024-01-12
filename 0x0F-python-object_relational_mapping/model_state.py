#!/usr/bin/python3
"""
A Python file containing class def of state
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer

Base = declarative_base()

class State(Base):
    """
    State class
    """
    __nameoftable__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
