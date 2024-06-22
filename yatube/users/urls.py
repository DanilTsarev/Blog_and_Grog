from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', views.signout, name='logout')
]