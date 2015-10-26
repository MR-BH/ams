#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The redis module'''
from .settings.utils import cache

def create_article_in_cache(article):
    '''Create article in cache

    :param article: the article to be created
    '''

    key = get_key_by_article_id(article.id)
    cache.hmset(key, {
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'category_id': article.category_id
    })

def update_article_in_cache(article):
    '''Mdoify article in cache

    :param article: the article to be modified
    '''

    key = get_key_by_article_id(article.id)
    cache.hmset(key, {
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'category_id': article.category_id
    })

def delete_article_in_cache(article_id):
    '''Delete article in cache

    :param id: the id of the article to be deleted
    '''

    key = get_key_by_article_id(article_id)
    cache.delete(key)

def read_article_from_cache(article_id):
    '''Create article in cache

    :param id: the id of the article to be readed
    '''

    key = get_key_by_article_id(article_id)
    article_read = cache.hgetall(key)
    print(article_read['content'])

def is_article_in_cache(article_id):
    '''Judge article in cache or not

    :param article_id: the id of the article be judged
    '''

    key = get_key_by_article_id(article_id)
    return cache.exists(key)

def get_key_by_article_id(article_id):
    return 'article:{0}'.format(article_id)
