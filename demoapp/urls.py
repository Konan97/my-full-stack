from django.urls import path
from demoapp import views

app_name = 'demoapp'
urlpatterns = [
    path('', views.home, name="home"),
    path('<name>/<int:price>', views.pathview, name = 'pathview'),
    path('getuser', views.qryview, name='qryview'),
]