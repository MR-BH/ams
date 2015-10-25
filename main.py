#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
'''help main module processing'''
import menu
from ams import ams


while True:
    menu.main_menu()
    instruct = raw_input('please press the number: ')
    # os.system('clear')
    if instruct == '0':
        comfir = raw_input('sure? <yes/no>: ')
        if comfir == 'y':
            quit()
        else:
            pass
    elif instruct == '1':
        # 调用create_new_article创建新的文章
        title = raw_input('plesae input title of the article: ')
        content = raw_input('pleasse input the content of the article: ')
        ams.show_all_category_and_id()
        category = raw_input('pleasw choose the category for che article: ')
        ams.create_new_article(title, content, category)
        print 'success'
    elif instruct == '2':
        #调用delete_article删除文章
        ams.show_article_name_with_id()
        article_id = raw_input('please input the id of the article you want to delete: ')
        ams.delete_article(article_id)
        print 'success'
    elif instruct == '3':
        #调用modify_article修改文章
        ams.show_article_name_with_id()
        id = raw_input('please input the id of the article you want to modify: ')
        title = raw_input('please input new title')
        content = raw_input('please input new connent: ')
        ams.show_all_category_and_id()
        category = raw_input('pleasw choose the category for che article: ')
        ams.modify_article(id, title, content, category)
        print 'success'
    elif instruct == '4':
        #调用read_article阅读文章
        ams.show_artile_name_with_id()
        article_id = raw_input('please input the id of the article you want to read: ')
        ams.read_article(article_id)
        print 'success'
    else:
        #输入指令错误
        print 'error instruct'

