from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://reqres.in/api/users/2')
    geodata = response.json()
    return render(request, {
        'ip': geodata['id'],
        'email': geodata['email'],
        'Fname': geodata['first_name'],
        'Lname': geodata['last_name'],
        'avtar':geodata['avatar']
    })