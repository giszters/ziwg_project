# -*- coding: UTF-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render_to_response, redirect

def logout_view(request):
    logout(request)
    return redirect('/login')

def home(request):
    print "tutej"
    return render_to_response("home.html", {'my_var': 3})
