from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('group/<slug:slug>/', views.group, name='group'),
    path('group/<slug:slug>/create', views.create, name='post_create'),
]