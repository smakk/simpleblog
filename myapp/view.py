from myapp import app
from flask.templating import render_template
from myapp.main_page_item import mainpage_info_item
from operator import attrgetter
from flask import g
from myapp.db_operations import *
from flask.globals import request
from flask.helpers import url_for

#main_items = mainpage_info_item('1','2','3','4','5','6','7','8','9','10',1)
#articles = []
#articles.append(main_items)

@app.route('/',methods = ['GET'])
def my_main_page():
    return render_template('type_articles.html' , nowposition = 'Linux' , 
                           items = sorted(articles , key = attrgetter('time'))[0:8],art_cls = article_types)
    return render_template('main.html',items = sorted(articles , key = attrgetter('time'))[0:8],\
                           remms = sorted(articles , key = attrgetter('recommand_star'))[0:5],\
                           art_cls = article_types)
    
@app.route('/<name>',methods = ['GET'])
def my_name(name):
    return render_template('newslistpic.html')