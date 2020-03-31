from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
from rest_framework.viewsets import ModelViewSet

from app01 import models

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from app01.serializers import UpdownSerializer

import json
# Create your views here.

def index(request):

    return render(request, "index.html")

def ajax_receive(request):

    return HttpResponse("hello")

def ajax_jquery(request):

    return render(request, "ajax_jquery.html")

def jquery_get(request):
    print(request.POST)

    dic={'name':"alex"}

    return HttpResponse(json.dumps(dic))

def up_down(request):

    data = models.App01DimStockUpdowns.objects.all()

    json_data = serializers.serialize('json', data)
    print(json_data)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)

class UpdownViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = models.App01DimStockUpdowns.objects.all()
    serializer_class = UpdownSerializer

class UpdownList(APIView):
    def get(self,request):
        queryset = models.App01DimStockUpdowns.objects.all()
        serializer = UpdownSerializer(queryset, many=True)
        print(request.GET)
        return Response(serializer.data)

    def post(self, request):
        serializer = UpdownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)