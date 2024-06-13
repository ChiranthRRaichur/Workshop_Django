from django.urls import path
from .import views

urlpatterns = [
    path("", views.welcome),
    path("app4/doctor1",views.doctor1, name='doc1'),
    path("app4/doctor2",views.doctor2, name='doc2'),
    path("app4/doctor3",views.doctor3, name='doc3'),
]