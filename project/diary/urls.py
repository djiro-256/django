from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),#/diaryで表示
    path('add/', views.add, name='add'),#/diary/add
]