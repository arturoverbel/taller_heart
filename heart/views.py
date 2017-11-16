# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from .models import Heart

def index(request):
    list = Heart.objects.order_by('-registered')[:50]
    return HttpResponse(serialize('json', list), content_type='json')

def save(request, dataA, dataB):
    h = Heart(registered=timezone.now(), dataA=dataA, dataB=dataB)
    h.save()

    return JsonResponse({'id': h.id })

