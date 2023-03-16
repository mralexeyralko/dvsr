from django.urls import path
from dvsr_mainpage import views

urlpatterns = [
    path('', views.mainpage, name='mainpage')
]