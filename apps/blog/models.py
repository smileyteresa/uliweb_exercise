# -*- coding: utf-8 -*-
from uliweb.orm import *

def blogs(Model):
    user_id = Field(INT)
    title = Field(CHAR)
    content = Field(TEXT)
    addtime = Field(datetime.datetime, auto_now_add = True)

def comments(Model):
    user_id = Field(INT)
    blog_id = Field(INT)
    content = Field(TEXT)
    addtime = Field(datetime.datetime, auto_now_add = True)