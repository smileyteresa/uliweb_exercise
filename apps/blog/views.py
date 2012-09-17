# -*- coding: utf-8 -*-
from uliweb import expose
from models import blogs, comments
from forms import BlogsForm, CommentsForm

@expose('/')
def index():
    form = BlogsForm()
    return {'form':form}