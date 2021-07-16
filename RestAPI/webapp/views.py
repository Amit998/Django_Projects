from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from  .models import Employee
from  .serializers import EmployeeSerializer


class EmployeeList(APIView):
    def get(self,request):
        EmployeeL=Employee.objects.all()
        serializer=EmployeeSerializer(EmployeeL,many=True)
        return Response(serializer.data)
    def post(self):
        pass
