from django.urls import path
from demoapp import views

app_name = 'demoapp'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('car/', views.cars), # API
    path('sf/', views.snowflake)
]