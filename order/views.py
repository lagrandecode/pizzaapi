from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response

# Create your views here.

class OrderView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'message':'order'},status=status.HTTP_200_OK)



class OrderCreateListView(generics.GenericAPIView):
    def get(self,request):
        pass

    def post(self,request):
        pass


class OrderDetailView(generics.GenericAPIView):
    def get(self,request,pk):
        pass 

    def put(self,request,pk):
        pass

    def delete(self,request,pk):
        pass