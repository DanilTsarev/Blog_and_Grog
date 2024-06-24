from django.contrib import admin
from django.urls import include, path

from posts.views import index

urlpatterns = [
    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]