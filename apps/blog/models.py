# -*- coding: utf-8 -*-
from uliweb.orm import *

class blogs(Model):
    username = Field(CHAR)
    title = Field(CHAR)
    content = Field(TEXT)
    addtime = Field(datetime.datetime, auto_now_add = True)

class comments(Model):
    username = Field(CHAR)
    blog_id = Field(int)
    content = Field(TEXT)
    addtime = Field(datetime.datetime, auto_now_add = True)