from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.db import IntegrityError
from .models import Car
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


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

@csrf_exempt
def cars(request):
    if request.method == 'GET':
        cars = Car.objects.all().values()
        return JsonResponse({"Cars": list(cars)})
    elif request.method == 'POST':
        name = request.POST.get('name')
        Rfid = request.POST.get('vehicle_type')
        ATACQ_Item = request.POST.get('ATACQ_Item')
        car = Car(
            name = name,
            Rfid = Rfid,
            ATACQ_Item = ATACQ_Item
        )
        try:
            car.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)

    return JsonResponse(model_to_dict(car), status=201) # create