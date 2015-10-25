#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ams.ams.db import Article
from ams.ams import redis_set


@pytest.fixture
def article_a_setup():
    arcicle = Article(id=10, title='test', content='test', category=1)
    return arcicle

def test_reate_article_in_cache(article_a_setup):
    redis_set.create_article_in_cache(article_a_setup)
    key = 'article:'+str(article_a_setup.id)
    assert redis_set.cache.hgetall(key)['id'] == '10'