from django.urls import path
from rest_framework.routers import DefaultRouter
from .view import snowflake
from .view import home

post_router = DefaultRouter()
post_router.register(r'posts', snowflake.ReactView, 'posts')

app_name = 'demoapp'
urlpatterns = [
    path('home/', home.home, name="home"),
    path('', snowflake.ReactView.as_view())
    #path('snowflake/', snowflake.snowflake)
]