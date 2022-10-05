import os

from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from openpyxl import load_workbook
# Create your views here.


class UsersAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserCreditsAPIView(generics.ListAPIView):
    """API view for user_credits_<user_id>. It returns all important information on credits of a certain user"""
    flag = True
    serializers_classes = (ExampleSerializer, ExampleSerializer)

    # One way to do it
    def list(self, request, *args, **kwargs):
        for i in args:
            print(i.actual_return_date)
            if i.actual_return_date == '1000-01-01':
                self.serializer_class = self.serializers_classes[0]
                return super().list(request, *args, **kwargs)

        self.serializer_class = self.serializers_classes[1]
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Credits.objects.filter(user_id_id=user_id)
        return queryset

    if flag:
        serializer_class = UserCreditsSerializer_true
    else:
        serializer_class = UserCreditsSerializer_false



class FileView(APIView):
    """API view for plans_insert. It downloads a xlsx file and works with it content"""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        basedir = '/home/oleg' #path to parent dir of test_zadaniye
        if file_serializer.is_valid():
            file_serializer.save()
            wb = load_workbook(filename=basedir + '/test_zadaniye'+file_serializer.data.get('file'))
            sheet_ranges = wb['Sheet1']
            if Plans.objects.filter(period=sheet_ranges['B2'].value, category_id=sheet_ranges['D2'].value):
                return Response('This data is already in database')
            elif sheet_ranges['B2'].value.strftime("%d") != '01':
                return Response('Not the first day of the month')
            elif sheet_ranges['C2'].value is None:
                return Response('Sum field is empty')
            else:
                Plans.objects.create(period=sheet_ranges['B2'].value, sum=sheet_ranges['C2'].value,
                                     category_id=Dictionary.objects.get(id=sheet_ranges['D2'].value))
            print('all_tests_are_done')
            return Response('New plan was added to database', status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

