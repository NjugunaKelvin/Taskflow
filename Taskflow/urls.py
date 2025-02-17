from django.contrib import admin
from django.urls import path, include
from tasks.views import custom_login, custom_logout, register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', register, name='register'), 
]

