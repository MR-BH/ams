#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''The module for modle layer'''
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Text, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from .settings import AMS_DB_SETTINGS


engine = create_engine(AMS_DB_SETTINGS)
DB_Session = sessionmaker(bind=engine)
# session = DB_Session()

BaseModel = declarative_base()


class Category(BaseModel):
    '''ORM for table category'''

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(64))


class Article(BaseModel):
    '''ORM for table article'''

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    category_id = Column(Integer, ForeignKey('category.id'))
    content = Column(Text)
    modify_at = Column(TIMESTAMP)


def create_article(title, content, category_id):
    '''Cerate new article

    :param title: the title of the article
    :param contnet: the content of the article
    :param category_id: the category id of the article
    :returns: the status code whether the article create success
    '''

    session = DB_Session()
    article = Article(title=title, content=content, category_id=category_id)
    status = 1
    try:
        session.add(article)
        session.commit()
    except:
        session.rollback()
        status = 0
        raise
    finally:
        session.close()
    return status


def delete_article(article_id):
    '''Delete article

    :param article_id: the id of the article
    :returns: the status code whether the article delete success
    :exception: delete error
    '''

    session = DB_Session()
    status = 1
    try:
        session.query(Article).filter(Article.id == article_id).delete()
        session.commit()
    except:
        session.rollback()
        status = 0
        raise
    finally:
        session.close()
    return status


def modify_article(article_id, title, content, category_id):
    '''Modify article

    :param article_id: the id of the article
    :param title: the title of the article
    :param contnet: the content of the article
    :param category_id: the category id of the article
    :returns: the article been modified
    :exception: modify error
    '''

    session = DB_Session()
    try:
        session.query(Article).filter(Article.id == article_id).update(
            {
                Article.title: title,
                Article.content: content,
                Article.category_id: category_id
            })
        article_modify = session.query(Article).filter(
            Article.id == article_id).first()
        session.commit()
    except:
        session.rollback()
        article_modify = None
        raise
    finally:
        session.close()
    return article_modify


def read_article(article_id):
    '''Read article

    :param article_id: the id of the article
    :returns: the article been readed
    '''

    session = DB_Session()
    article_read = session.query(Article).filter(
        Article.id == article_id).first()
    print article_read.content
    session.close()
    return article_read


def show_article_name_with_id():
    '''Show all article name with id'''
    session = DB_Session()
    articles = session.query(Article).all()
    session.close()
    for article in articles:
        print(article.id, article.title)


def show_all_category_and_id():
    '''Show all category name with id'''
    session = DB_Session()
    categorys = session.query(Category).all()
    for category in categorys:
        print(category.id, category.category_name)
