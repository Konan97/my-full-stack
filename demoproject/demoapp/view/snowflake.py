"""django imports"""
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import *
from ..serializer import *

"""snowflake imports"""
from snowflake.snowpark import Session

class ReactView(APIView):
    # def snowflake(request):
    #     user = "YSUN98@VOLVOCARS.COM"
    #     account = "VOLVOCARS-MANUFACTURINGANALYTICS"
    #     connection_params = {
    #     "user": user,
    #     "account":account,
    #     "authenticator":"externalbrowser",
    #     "warehouse": "REPORTING",
    #     "database": "VCC",
    #     "schema":"PRD_CASTLE_DESIGN"
    #     }
    #     session = Session.builder.configs(connection_params).create()
    #     SQL_query = "Select DISTINCT 'Rfid' from \"DESIGN_ATACQ_ITEM_ON_CAR_ALL_SHOPS\" Where \"Plant\" = 'VCCH' AND \"Main Type Description\" = 'EX90' AND \"ATACQ Item Family English Desc\" = 'A-SHOP FAULTS' AND \"Link Timestamp\" >= '2024-03-05 00:00:00.000'"
    #     df_sql = session.sql(SQL_query)
    #     df_sql.show()
    #     session.close()
    #     return render(request, "index.html", connection_params)
    
    def get(self, request):
        output = {"user": "example"}
        return Response(output)
    
    def post(self, request):
        serialized_item = UserSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)