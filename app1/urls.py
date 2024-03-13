from django.urls import path
from app1.views import lista , EmpleoListView
from rest_framework import  routers


urlpatterns = [
    path("modelo/",lista.as_view({"get":"list"}) , name="lista"),
    path("modelo/crear/",lista.as_view({"post":"create"}) , name="crear"),
    path("modelo/<int:pk>",lista.as_view({"get":"retrieve"}) , name="detalle"),
    path("modelo/<int:pk>/update",lista.as_view({"put":"update"}) , name="update"),
    path("modelo/<int:pk>/eliminar",lista.as_view({"delete":"destroy"}) , name="eliminar"),
    path("empleo",EmpleoListView.as_view(),name="empleo")
]

