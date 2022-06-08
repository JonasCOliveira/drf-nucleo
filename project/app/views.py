import io
import json
from rest_framework import  viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework import generics, views, viewsets, filters, status, exceptions, authentication
from rest_framework.authentication import SessionAuthentication,BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from datetime import timedelta, datetime


from app.models import *
from app.serializers import *

@api_view(['GET', 'POST'])
def lista_descargas(request):

    response = []
    try:
        descargas = Descargas.objects.all()
    except Descargas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        for d in descargas: 
            obj = {
                "type": "FeatureCollection",
                "features": [
                    {
                    "type": "Feature",
                    "properties": {
                        "hora": d.timestamp.hour,
                        "minuto": d.timestamp.minute,
                        "segundo": d.timestamp.second,
                        "intensidade": d.intensidade,
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [d.latitude, d.longitude]
                    }
                    }
                ]
                }
            response.append(obj)
        return Response(response)
    
    if request.method == 'POST':
        serializer = DescargasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def lista_descargas_ultima_hora(request):

    response = []
    try:
        descargas = Descargas.objects.filter(timestamp__gte = (datetime.now() - timedelta(hours=1)))
    except Descargas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        for d in descargas: 
            obj = {
                "type": "FeatureCollection",
                "features": [
                    {
                    "type": "Feature",
                    "properties": {
                        "hora": d.timestamp.hour,
                        "minuto": d.timestamp.minute,
                        "segundo": d.timestamp.second,
                        "intensidade": d.intensidade,
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [d.latitude, d.longitude]
                    }
                    }
                ]
                }
            response.append(obj)
        return Response(response)

@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_descarga(request, id):

    try:
        # descargas = Descargas.objects.filter(timestamp__gte = datetime.now() - timedelta(hours=1))
        descarga = Descargas.objects.get(id=id)
    except Descargas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
            obj = {
                "type": "FeatureCollection",
                "features": [
                    {
                    "type": "Feature",
                    "properties": {
                        "hora": descarga.timestamp.hour,
                        "minuto": descarga.timestamp.minute,
                        "segundo": descarga.timestamp.second,
                        "intensidade": descarga.intensidade,
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [descarga.latitude, descarga.longitude]
                    }
                    }
                ]
                }

            return Response(obj)

    if request.method == 'PUT':
        serializer = DescargasSerializer(descarga, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        descarga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

@api_view(['GET', 'POST'])
def lista_alvos(request):
    response = []
    try: 
        alvos = Alvo.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        for a in alvos:
            obj =   {
                "type": "FeatureCollection",
                "properties": {"empresa" : Empresa.objects.get(id=a.empresa_id).descricao, "nome": a.nome}, #, 
                "features": [{
                "type": "Feature",
                "geometry": { "type": "LineString", "coordinates": [a.coordenadas] },
                "properties": { "buffer": Buffer.objects.get(id=a.buffer_id).tipoBuffer }, #
                "id": a.id
                }]
            }
            response.append(obj)
        return Response(response)
    
    if request.method == 'POST':
        serializer = AlvoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_alvo(request, id):
    try: 
        alvo = Alvo.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        obj =   {
                "type": "FeatureCollection",
                "properties": {"empresa" : Empresa.objects.get(id=alvo.empresa_id).descricao, "nome": alvo.nome}, #, 
                "features": [{
                "type": "Feature",
                "geometry": { "type": "LineString", "coordinates": [alvo.coordenadas] },
                "properties": { "buffer": Buffer.objects.get(id=alvo.buffer_id).tipoBuffer }, #
                "id": alvo.id
                }]
            }
        return Response(obj)

    if request.method == 'PUT':
        serializer = AlvoSerializer(alvo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        alvo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

