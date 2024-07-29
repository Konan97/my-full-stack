from django.urls import path
from .view import snowflake
from .view import home

app_name = 'demoapp'
urlpatterns = [
    path('home/', home.home, name="home"),
    path('car/', snowflake.cars), # API
    path('snowflake/', snowflake.snowflake)
]