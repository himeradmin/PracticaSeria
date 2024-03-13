from django.shortcuts import render , get_object_or_404
from rest_framework import  viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Personal, Empleo
from .serializers import PersonalSerializers
from app1.Serializador.serializador_empleo import EmpleoSerializers
# Create your views here.


class EmpleoListView(generics.ListAPIView):
    serializer_class = EmpleoSerializers
    def get_queryset(self):
        model= Empleo.objects.all()
        return  model

class CrearListviews(generics.ListCreateAPIView):
    queryset = Empleo.objects.filter()
    serializer_class = EmpleoSerializers

class DetalleViews(generics.RetrieveDestroyAPIView):
    queryset = Empleo.objects.all()
    serializer_class = EmpleoSerializers

class lista(viewsets.ViewSet):
    def list(self,request):
        model= Personal.objects.all()
        serializador= PersonalSerializers(model,many=True)
        return  Response(serializador.data)
    def create(self,request):
        serialiador= PersonalSerializers(data=request.data)
        if serialiador.is_valid():
            serialiador.save()
            return Response("Creado Correctamente", status=status.HTTP_200_OK)
        return Response(serialiador.errors)

    def retrieve(self,request,pk=None):
        model= Personal.objects.all()
        dato= get_object_or_404(model,pk=pk)
        serializado= PersonalSerializers(dato)
        return Response(serializado.data, status=status.HTTP_200_OK)

    def update(self,request,pk=None):
        queryset= Personal.objects.filter(pk=pk).first()
        serializado= PersonalSerializers(queryset,data=request.data)
        if serializado.is_valid():
            serializado.save()
            return  Response(serializado.data)
        return Response(serializado.errors)
    def destroy(self , request, pk=None):
        model= Personal.objects.filter(pk=pk)
        model.delete()
        return Response("Eliminado")







