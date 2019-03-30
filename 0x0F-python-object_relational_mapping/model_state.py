#!/usr/bin/python3
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class that inherits from base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
