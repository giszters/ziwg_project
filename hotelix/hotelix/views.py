# -*- coding: UTF-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render_to_response, redirect


def logout_view(request):
    logout(request)
    return redirect('/login')


def home(request):
    return render_to_response("home.html", {'my_var': 3})


class SuccessMixin(object):
    def get_success_url(self):
        return super(SuccessMixin, self).get_success_url() + "?success=1"


def compute_lightness(breadcrums_list):
    l = len(breadcrums_list)
    for i in xrange(l):
        # magic, huh?
        breadcrums_list[i]['lightness'] = str("%.1f" % (40 + (50.0/l)*i))
        breadcrums_list[i]['fontcolor'] = str("0, 100%%, %.1f%%, 1" % (100 - (70.0/l)*i))
    return breadcrums_list
            
