#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ams.ams.db import Article
from ams.ams import db
from ams.ams import ams

def article_a_teardown():
    session = db.DB_Session()
    session.query(Article).filter(Article.title=='test',
                                  Article.content=='test',
                                  Article.category==1).delete()
    session.commit()
    session.close()

@pytest.fixture
def article_a_setup(request):
    arcicle = Article(title='test', content='test', category=1)
    request.addfinalizer(article_a_teardown)
    return arcicle

@pytest.fixture
def article_no_teardown_a_setup():
    article = Article(id=10,title='test2', content='test2', category=1)
    return article

def test_reate_article_in_cache(article_a_setup):
    ams.create_new_article(article_a_setup.title,
                           article_a_setup.content,
                           article_a_setup.category)
    session = db.DB_Session()
    query = session.query(Article).filter(Article.title==article_a_setup.title,
                                          Article.content==article_a_setup.content,
                                          Article.category==article_a_setup.category).first()
    session.close()
    assert query.id != None

def test_delete_article(article_no_teardown_a_setup):
    session = db.DB_Session()
    session.add(article_no_teardown_a_setup)
    session.commit()
    ams.delete_article(10)
    assert session.query(Article).filter(Article.id==10).first() == None
    session.close()


