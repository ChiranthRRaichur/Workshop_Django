from django.urls import path
from .import views

urlpatterns = [
    path("", views.icici, name='icici'),
    # path("print_id", views.print_id, name='print_id')
    # path("print_id/<int:id>/", views.print_id, name='print_id')
]
