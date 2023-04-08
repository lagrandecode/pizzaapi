from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Order

# Create your views here.


class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    def get(self,request):
        order = Order.objects.all()
        serializer = self.serializer_class(order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    def get(self,request,pk):
        pass 

    def put(self,request,pk):
        pass

    def delete(self,request,pk):
        pass