from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Order
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

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


class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.UpdateOrderSerializer
    def put(self,request,pk):
        order = get_object_or_404(Order,id=pk)
        serializer = self.serializer_class(data=request.data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class OrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    def get(self,request,pk):
        user = User.objects.get(id=pk)
        order = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class OrderDetailSpecificView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    def get(self,request,user_id,order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(serializer.data,status=status.HTTP_200_OK)
