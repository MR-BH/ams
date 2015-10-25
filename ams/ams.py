#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The module request to set uo cache and ORM'''
from db import  DB_Session, Article, Category
import redis_set


def create_new_article(title, content, category):
    '''Cerate new article

    :param title: the title of the article
    :param contnet: the content of the article
    :param category: the category id of the article
    '''

    session = DB_Session()
    article1 = Article(title=title, content=content, category=category)
    session.add(article1)
    redis_set.create_article_in_cache(article1)
    session.commit()
    session.close()

def delete_article(id):
    '''Delete article

    :param id: the id of the article
    '''

    session = DB_Session()
    session.query(Article).filter(Article.id == id).delete()
    redis_set.delete_article_in_cache(id)
    session.commit()
    session.close()

def modify_article(id, title, content, category):
    '''Modify article

    :param id: the id of the article
    :param title: the title of the article
    :param contnet: the content of the article
    :param category: the category id of the article
    '''

    session = DB_Session()
    session.query(Article).filter(Article.id == id).update(
        {
            Article.title: title,
            Article.content: content,
            Article.category: category
        })
    article1 = session.query(Article).filter(Article.id == id).first()
    redis_set.update_article_in_cache(article1)
    session.commit()
    session.close()

def read_article(id):
    '''Read article

    :param id: the id of the article
    '''

    if redis_set.is_article_in_cache(id):
        redis_set.read_article_from_cache(id)
    else:
        session = DB_Session()
        article_read = session.query(Article).filter(Article.id == id).first()
        redis_set.create_article_in_cache(article_read)
        print article_read.content
        session.close()

def show_article_name_with_id():
    '''Show all article name with id'''
    session = DB_Session()
    query = session.query(Article).all()
    for article1 in query:
        print(article1.id, article1.title)

def show_all_category_and_id():
    '''Show all category name with id'''
    session = DB_Session()
    query = session.query(Category).all()
    for category1 in query:
        print(category1.id, category1.category_name)
