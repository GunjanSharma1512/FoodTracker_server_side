# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from requests import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from models import *

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import smtplib
import requests
import json
from django.core.mail import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#def sendNotif():


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def getDonorData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')

        donorDataObj = DonorData()
        donorDataObj.name=name
        donorDataObj.quantity=quantity
        donorDataObj.description=description
        donorDataObj.save(force_insert=True)

      #  sendNotif()
        return Response("donor data stored")

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def viewDonorData(request):
    if request.method == 'POST':
        all_obj = DonorData.objects.all()
        myList=[]

        for obj in all_obj:
            myDict={}
            myDict['name']=obj.name
            myDict['quantity']=obj.quantity
            myDict['description']=obj.description
            myList.append(myDict)


        return Response(myList)
