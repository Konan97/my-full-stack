from django.urls import path
from demoapp import views

app_name = 'demoapp'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('getuser/', views.qryview, name='qryview'),
    path('car/', views.cars) # API
]