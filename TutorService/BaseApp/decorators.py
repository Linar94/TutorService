__author__ = '12'
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from BaseApp.models import Tutor
from django.core.exceptions import ObjectDoesNotExist


def no_login_please(f):
    def wrapper(request, *args, **kargs):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse("tutor_service:homepage"))
        else:
            return f(request, *args, **kargs)

    return wrapper


def check_add_subject__for_tutor(f):
    def wrapper(self, request, *args, **kwargs):
        try:
            Tutor.objects.get(username=self.request.user.id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse("tutor_service:homepage"))
        return f(self, request, *args, **kwargs)

    return wrapper


def check_questionnaire__for_tutor(f):
    def wrapper(request):
        try:
            Tutor.objects.get(username=request.user.id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse("tutor_service:homepage"))
        return f(request)

    return wrapper

def is_anonymous(f):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous():
            return f(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("tutor_service:homepage"))
    return wrapper