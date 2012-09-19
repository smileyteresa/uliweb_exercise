# -*- coding: utf-8 -*-
from uliweb.form import *

class BlogsForm(Form):
    title    =  StringField(label = "标题", required = True)
    content  =  TextField(label = "内容", required = True, rows = 10,cols = 60)

class CommentsForm(Form):
    username = StringField(label = "昵称", required =True)
    content = TextField(label = "评论", required = True, cols = 60)