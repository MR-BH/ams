#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The module request to set uo cache and ORM'''

import redis_set
import models

def create_new_article(title, content, category_id):
    '''Cerate new article

    :param title: the title of the article
    :param contnet: the content of the article
    :param category_id: the category id of the article
    :returns: the status code whether the article create success
    '''

    return models.create_article(title, content, category_id)



def delete_article(article_id):
    '''Delete article

    :param article_id: the id of the article
    :returns: the status code whether the article delete success
    '''

    if models.delete_article(article_id):
        if redis_set.is_article_in_cache(article_id):
            redis_set.delete_article_in_cache(id)
        return 1
    else:
        return 0

def modify_article(article_id, title, content, category_id):
    '''Modify article

    :param article_id: the id of the article
    :param title: the title of the article
    :param contnet: the content of the article
    :param category_id: the category id of the article
    :returns: the status code whether the article modify success
    '''

    article = models.modify_article(article_id, title, content, category_id)
    if article is not None:
        redis_set.update_article_in_cache(article)
        print 'success'
        return 1
    else:
        print 'modify fail'
        return 0

def read_article(article_id):
    '''Read article

    :param id: the id of the article
    '''

    if redis_set.is_article_in_cache(article_id):
        redis_set.read_article_from_cache(article_id)
    else:
        article = models.read_article(article_id)
        if article is not None:
            redis_set.create_article_in_cache(article)
        else:
            print "read error"



def show_article_name_with_id():
    '''Show all article name with id'''
    models.show_article_name_with_id()

def show_all_category_and_id():
    '''Show all category name with id'''
    models.show_all_category_and_id()
