# -*- coding: utf-8 -*-
from uliweb import expose
from models import blogs, comments
from forms import BlogsForm, CommentsForm
from uliweb import function
require_login = function("require_login")
from uliweb.contrib.auth.views import login

@expose('/')
def index():
    blog = blogs.all()
    return {'blog':blog}

@expose('/create')
def create():
    if require_login():
        return redirect(url_for(login))

    if request.method == "POST":
        form = BlogsForm()
        flag = form.validate(request.params)
        if flag:
            info = blogs(**form.data)
            info.username = request.user.username
            info.save()
        return redirect('/view/%d' % info.id)

    form = BlogsForm()
    return {'form':form}

@expose('/view/<id>')
def view(id):
    if request.method == "GET":
        info = blogs.get(blogs.c.id == id)
        form = CommentsForm()
        comment = comments.filter(comments.c.blog_id == id)
        return {'form':form, 'info':info, 'comment':comment}

    if request.method == "POST":
        form = CommentsForm()
        flag = form.validate(request.params)
        if flag:
            info = comments(**form.data)
            info.blog_id = id
            info.save()
        return redirect('/view/%s' % id)

@expose('/edit/<id>')
def edit():
    pass

@expose('/delete/<id>')
def delete():
    pass