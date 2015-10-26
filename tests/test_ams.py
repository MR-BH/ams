#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ams.ams.models import Article
from ams.ams import models
from ams.ams import ams

def article_a_teardown():
    session = models.DB_Session()
    session.query(Article).filter(Article.title=='test',
                                  Article.content=='test',
                                  Article.category_id==1).delete()
    session.commit()
    session.close()

@pytest.fixture
def article_a_setup(request):
    arcicle = Article(title='test', content='test', category_id=1)
    request.addfinalizer(article_a_teardown)
    return arcicle

@pytest.fixture
def article_no_teardown_a_setup():
    article = Article(id=10,title='test2', content='test2', category_id=1)
    return article

def test_reate_article_in_cache(article_a_setup):
    ams.create_new_article(article_a_setup.title,
                           article_a_setup.content,
                           article_a_setup.category_id)
    session = models.DB_Session()
    query = session.query(Article).filter(Article.title==article_a_setup.title,
                                          Article.content==article_a_setup.content,
                                          Article.category_id==article_a_setup.category_id).first()
    session.close()
    assert query.id != None

def test_delete_article(article_no_teardown_a_setup):
    session = models.DB_Session()
    session.add(article_no_teardown_a_setup)
    session.commit()
    ams.delete_article(10)
    assert session.query(Article).filter(Article.id==10).first() == None
    session.close()



