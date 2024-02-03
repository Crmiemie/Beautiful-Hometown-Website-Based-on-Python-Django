from django.urls import path
from . import views

app_name = 'govern'

urlpatterns = [
    path('show', views.get_news, name='news'),
    path('cloud',views.cloud,name='cloud')
]