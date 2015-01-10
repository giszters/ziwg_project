# -*- coding: UTF-8 -*-
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.views.generic import TemplateView


def logout_view(request):
    logout(request)
    return redirect('/login')

"""
def home(request):
    return render_to_response("home.html", {'my_var': 3, 'user': request.user})
"""
class EasyHome(TemplateView):
    template_name = 'base.html'
    

#def page404(request):
#   return render_to_response("404.html", {'user': request.user})


class SuccessMixin(object):
    def get_success_url(self):
        return super(SuccessMixin, self).get_success_url() + "?success=1"


class PermMixin(object):
    def get(self, request, *args, **kwargs):
        if self.perm_name is None:
            raise Exception(u"perm_name for this view is None")
        perm = self.__module__.split(".")[0] + "." + self.perm_name
        if not request.user.has_perm(perm):
            raise Http404(u"Nie masz uprawnienia do oglądania tego zasobu")
        print u"uprawnienie przeszło"
        return super(PermMixin, self).get(request, *args, **kwargs)


def compute_lightness(breadcrums_list):
    l = len(breadcrums_list)
    for i in xrange(l):
        # magic, huh?
        breadcrums_list[i]['lightness'] = str("%.1f" % (40 + (50.0/l)*i))
        breadcrums_list[i]['fontcolor'] = str("0, 100%%, %.1f%%, 1" % (100 - (70.0/l)*i))
    return breadcrums_list
            
