from django.shortcuts import render
import requests
import random
import moment
import json
from django.http import HttpResponse

def getrequest(request):
    response = requests.get('https://reqres.in/api/users/2')
    geodata = response.json()
    return render(request, {
        'ip': geodata['id'],
        'email': geodata['email'],
        'Fname': geodata['first_name'],
        'Lname': geodata['last_name'],
        'avtar':geodata['avatar']
    })


def postrequest(request):

    post_data = {
        'users': 'Rocky',
        'id': random.randint(1, 999),
        'createdAt': str(moment.utcnow())
    }
    response = requests.post('https://reqres.in/api/users',data=post_data)
    #geodata = response.json()
    json_data = json.dumps(post_data)
    return HttpResponse(request,json_data, content_type='application/json')