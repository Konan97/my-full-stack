from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from datetime import timedelta
from typing import List

from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.core import Root,CreateMode
from snowflake.core.database import Database
from snowflake.core.schema import Schema
from snowflake.core.table import Table, TableColumn, PrimaryKey
from snowflake.core.warehouse import Warehouse
from snowflake.core._common import CreateMode
from snowflake.core.task import StoredProcedureCall, Task
from snowflake.core.task.dagv1 import DAGOperation, DAG, DAGTask

from .models import Car

def snowflake(request):
    user = "YSUN98@VOLVOCARS.COM"
    connection_params = {
    "user": user,
    "account":"VOLVOCARS-MANUFACTURINGANALYTICS",
    "authenticator":"externalbrowser",
    "warehouse": "REPORTING",
    "database": "VCC",
    "schema":"PRD_CASTLE_DESIGN"
    }
    session = Session.builder.configs(connection_params).create()
    root = Root(session)
    return render(request, "index.html", connection_params)


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
    about_content = {'time': time, 'path': path, 'method': method}
    return render(request, 'index.html', {'content': about_content})

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