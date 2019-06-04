from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import datetime
import moment
import requests
from django.shortcuts import render


# Create your views here.


def post(request):

    post_data = {
        'users': 'Rocky',
        'id': random.randint(1, 999),
        'createdAt': str(moment.utcnow())
    }
    response = requests.post('https://reqres.in/api/users',data=post_data)
    #geodata = response.json()
    json_data = json.dumps(post_data)
    return HttpResponse(request,json_data, content_type='application/json')


"""def post(requests):
    post_data={
        'users':'Rocky',
        'id':random.randint(1,999),
        'createdAt':str(moment.utcnow())

    }
    json_data=json.dumps(post_data)
    return HttpResponse(json_data,content_type='application/json')"""