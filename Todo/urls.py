"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_app.views import *
from todo_app.views import *
from todo_sam.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign/',RegistrationView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('add/',TakAdd.as_view(),name ="add"),
    path('list/<int:pk>',ListTask.as_view()),
    path('delete/<int:pk>',DeleteView.as_view(),name="delete"),
    path('update/<int:pk>',UpdateView.as_view(),name="update"),
    path("",BaseView.as_view(),name="home"),
    path("complete/<int:pk>",TaskComplete.as_view(), name="complete"),
    path('listcreatee/',TodolistCreateView.as_view())
    
]
