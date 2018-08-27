import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.staticfiles.templatetags.staticfiles import static

from licence.models import Composition

from polls.models import Question

# Create your views here.
def test(request, id_licence = 0):
    datas = {}
    i = 0
    compositions = list(Composition.objects.all().filter(licence=id_licence))

    for comp in compositions:
        datas[comp.id] = {'pk': comp.id, 'name': comp.name, 'price':str(comp.price), 'data': []}

    for comp in compositions:
        for item in comp.itemcomposition_set.all():
            datas[item.composition_id]['data'].append(item.item)
            i += 1

        i = 0

    renderDatas = json.dumps(datas)
    return HttpResponse(renderDatas)

def quiz(request):
    count = Question.objects.filter().count()
    question = None
    choices = []

    while question is None:
        value = randint(0, count)
        try:
            question = Question.objects.get(pk=value)
        except ObjectDoesNotExist:
            question = None


    choice = question.choice_set.all()

    for x in range(0, choice.count()):
        list = {
            "value": choice[x].pk,
            "text": choice[x].choice_text
        }
        choices.append(list)

    datas = {'question': question.question_text, 'media': static('upload/%s' % question.media_url), 'choice': choices}

    renderDatas = json.dumps(datas)
    return HttpResponse(renderDatas)
