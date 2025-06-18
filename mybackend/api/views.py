from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .models import *
from .serializers import *


from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@api_view(['POST'])
def createuser(request):
 if request.method =='POST':
 
     Firstname = request.data.get('firstname')
     Lastname = request.data.get('lastname')
     regemail = request.data.get('regemail')
     regpassword = request.data.get('regpassword')  
     if RegisterUser.objects.filter(regemail=regemail).exists():
         return Response({"message":'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
     user = RegisterUser.objects.create(
     
        Firstname = Firstname,
        Lastname = Lastname,
        regemail = regemail,
        regpassword = make_password(regpassword)
     )
     serializer= RegisterUserSerializer(data=user)
     if serializer.is_valid():
        serializer.save()
        return Response({"message":"User Created Successfulyy"},serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
@permission_classes([AllowAny])
def loginuser(request):
   username = request.data.get('username')
   password = request.data.get('regpassword')
   user = authenticate(username=username, password=password)
   if user:
      refresh = RefreshToken.for_user(user)
      return Response({
         'refresh':str(refresh),
         'access':str(refresh.access_token),
         'user':{
            'id':user.id,
            'username':user.username,
            'email':user.regemail,
         }
      })
   else:
      return Response({"message":"Invalid Credentials"}, status = status.HTTP_401_UNAUTHORIZED)
@api_view(['POST','GET'])
def registercategory(request):
   data = request.data
   if request.method == "POST":
      serializer = RegisterCategorySerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response( serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == "GET":
      data = RegisterCategory.objects.all()
      serializer = RegisterCategorySerializer(data, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['POST','GET'])
def registerbrand(request):
   if request.method =="POST":
      data = request.data
      serializer = RegisterBrandSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == "GET":
      data = RegisterBrand.objects.all()
      serializer = RegisterBrandSerializer(data, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
   
@api_view(['POST','GET'])
@parser_classes([MultiPartParser, FormParser])
def registerproduct(request):
   if request.method =="POST":
      data = request.data
      serializer = AddProductSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == "GET":
      data = Addproduct.objects.all()
      serializer = AddProductSerializer(data, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)