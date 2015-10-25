#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The redis module'''
import redis

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def create_article_in_cache(article):
    '''Create article in cache

    :param article: the article to be created
    '''

    key = 'article:'+str(article.id)
    cache.hmset(key,{
        'id':article.id,
        'title':article.title,
        'content':article.content,
        'category':article.category
    })
def update_article_in_cache(article):
    '''Mdoify article in cache

    :param article: the article to be modified
    '''

    key = 'article:'+str(article.id)
    cache.hmset(key,{
        'id':article.id,
        'title':article.title,
        'content':article.content,
        'category':article.category
    })

def delete_article_in_cache(id):
    '''Delete article in cache

    :param id: the id of the article to be deleted
    '''

    key = 'article:'+str(id)
    cache.delete(key)

def read_article_from_cache(id):
    '''Create article in cache

    :param id: the id of the article to be readed
    '''

    key = 'article:'+str(id)
    article_read = cache.hgetall(key)
    print(article_read['content'])

def is_article_in_cache(id):
    '''Judge article in cache or not

    :param article: the id of the article be judged
    '''

    key = 'article:'+str(id)
    return cache.exists(key)


