from django.urls import path
from demoapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<name>/<int:price>', views.pathview, name = 'pathview'),
    path('getuser', views.qryview, name='qryview'),
    path('ratings', views.RatingsView.as_view()),
]