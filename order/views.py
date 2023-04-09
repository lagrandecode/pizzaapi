from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Order
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self,request):
        order = Order.objects.all()
        serializer = self.serializer_class(order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    def get(self,request,pk):
        order = get_object_or_404(Order,id=pk) 
        serializer = self.serializer_class(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        order = get_object_or_404(Order,id=pk)
        serializer = self.serializer_class(data=request.data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        order = get_object_or_404(Order,id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)