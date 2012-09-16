# -*- coding: utf-8 -*-
from uliweb import expose
from models import blogs, comments
from forms import BlogsForm, CommentsForm

@expose('/')
def index():
    blog = blogs.all()
    form = BlogsForm()
    return {'blog':blog, 'form':form}