from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice

# Create your views here.
def test(request, id_licence):
    return HttpResponse("You're looking at question %s" % id_licence)
