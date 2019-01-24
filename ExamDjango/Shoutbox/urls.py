from django.urls import path

from . import views

app_name = 'Shoutbox'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('', views.submit, name='submit')
]
