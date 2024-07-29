"""django imports"""
from django.shortcuts import render

"""snowflake imports"""
from snowflake.snowpark import Session

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
