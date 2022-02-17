from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
path('login', views.login, name='login'),
path('logout', views.login, name='logout'),
path('register', views.register, name='register'),
path('createproduct',views.createproduct , name='createproduct')
]