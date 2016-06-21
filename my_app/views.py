from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from collections import OrderedDict

# Create your views here.

@csrf_exempt
def home(request):
    x = json.loads(request.body)
    y = x.get('string')
    to_list = y.split()
    new_list = [i.strip(',.') for i in to_list]
    result = OrderedDict()
    for i in new_list:
        result[i] = new_list.count(i)
    return HttpResponse(json.dumps(result), content_type="application/json")
