#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The sqlalchemy module to ORM'''
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, Text, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey



DB_CONNECT_STRING = \
    'mysql+pymysql://eleme:eleme@localhost/article_manage?charset=utf8'
engine = create_engine(DB_CONNECT_STRING)
DB_Session = sessionmaker(bind=engine)
# session = DB_Session()

BaseModel = declarative_base()

class Category(BaseModel):
    '''ORM for table category'''

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(CHAR(45))

class Article(BaseModel):
    '''ORM for table article'''

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(CHAR(45))
    category = Column(Integer, ForeignKey('category.id'))
    content = Column(Text)
    modify_at = Column(TIMESTAMP)
