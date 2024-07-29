"""django imports"""
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from datetime import timedelta
from typing import List

"""snowflake imports"""
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

from ..models import Car

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
    df_sql = session.sql("Select DISTINCT 'Rfid' from \"DESIGN_ATACQ_ITEM_ON_CAR_ALL_SHOPS\" Where \"Plant\" = 'VCCH' AND \"Main Type Description\" = 'EX90' AND \"ATACQ Item Family English Desc\" = 'A-SHOP FAULTS' AND \"Link Timestamp\" >= '2024-03-05 00:00:00.000'")
    df_sql.show()
    session.close()
    return render(request, "index.html", connection_params)

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