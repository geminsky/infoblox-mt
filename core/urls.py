from django.urls import path, re_path
from . import views

app_name = 'core'

urlpatterns = [
    path('all', views.UserDataAPI.as_view(), name='user-list'),
    path('new', views.UserDataAddAPI.as_view(), name='user-create'),
]