# -*- coding: utf-8 -*-
from uliweb.form import *

class BlogsForm(Form):
    title = StringField(label = "标题", required = True)
    content = TextField(label = "内容", required = True)

class CommentsForm(Form):
    content = TextField(label = "评论", required = True)