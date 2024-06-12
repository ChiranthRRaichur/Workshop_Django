from django.urls import path
from . import views

urlpatterns =[
    path("sqr/",views.sqr),
    path("getFact/",views.getFact),
]