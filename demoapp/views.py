from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def pathview(request, name, price):
    items = {
        'URL' : 'uniform resource locator'
    }
    description = items[name]
    return HttpResponse(f"<h2>{name}<h2>" + description)
# Create your views here.

def home(request):
    time = datetime.today()
    path = request.path
    method = request.method
    content = '''
    <center><h2>Http Request Response</h2>
    <p>time: {}</p>
    <p>path: " {}</p>
    <p>method: {}</p></center>
    '''.format(time, path, method)
    
    return HttpResponse(content)