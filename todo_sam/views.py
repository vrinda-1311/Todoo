from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from todo_sam.models import TodoModel

from todo_sam.serializers import Todoserializer

from rest_framework import status

from django.shortcuts import get_object_or_404

# Create your views here.

class TodolistCreateView(APIView):

    def get(self,request): # used to list all the data from db to the client as response

        details = TodoModel.objects.all() # get all objects from the model

        seriazliers = Todoserializer(details, many = True) # convert into json

        return Response(seriazliers.data)
    
    def post(self,request):

        serializer = Todoserializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
  
class TodoupdateretrivedeleteView(APIView):

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        student = get_object_or_404(TodoModel,id=id)

        serializer = Todoserializer(student,many = False)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):

        id = kwargs.get('pk')

        data = get_object_or_404(TodoModel,id = id)

        serializer = Todoserializer(data,data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,**kwargs):

        id = kwargs.get('pk')

        data = get_object_or_404(TodoModel,id=id)

        data.delete()

        return Response({"message":"object deleted successfully"},status=status.HTTP_200_OK)




