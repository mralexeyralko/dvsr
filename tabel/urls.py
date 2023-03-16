from django.urls import path
from tabel import views

urlpatterns = [
    path('', views.tabel, name='tabel')
]