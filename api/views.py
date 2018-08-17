import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers

from licence.models import Composition

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
