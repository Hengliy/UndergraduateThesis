from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View
from utils.response import wrap_json_response, ReturnCode, CommonResponseMixin
from utils.auth import already_authorized, c2s
from app01.models import Tbluserinfo

class UserView(View, CommonResponseMixin):
    # 获取用户信息
    def get(self, request):
        # if not already_authorized(request):
        #     response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
        #     return JsonResponse(response, safe=False)

        ID=request.session.get('ID')
        data=Tbluserinfo.objects.filter(id=ID).values()

        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, data=list(data))
        return JsonResponse(response, safe=False)

    #修改信息
    def put(self, request):

        ID = request.session.get('ID')

        # got str object
        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)

        obj=Tbluserinfo.objects.filter(id=ID).update(**received_body)

        message = 'modify user info success.'
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(response, safe=False)

    #新建用户
    def post(self,request):
        # if not already_authorized(request):
        #     response = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
        #     return JsonResponse(response, safe=False)

        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)
        received_body['delflag'] = '0'
        received_body['verifyflag'] = '1'
        Tbluserinfo.objects.create(**received_body)

        message = 'create new user success.'
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(response, safe=False)
    def delete(self,request):
        ID = request.session.get('ID')
        obj = Tbluserinfo.objects.filter(id=ID).update(delflag=1)
        message = 'delete user info success.'
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(response, safe=False)


def isExist(request):
    if request.method=="GET":
        usericode=request.GET.get('usericode')
        try:
            Tbluserinfo.objects.get(usericode=usericode)
            message = 'already exist a user.'
            response = CommonResponseMixin.wrap_json_response(code=ReturnCode.FAILED, message=message)
            return JsonResponse(response, safe=False)
        except:
            message = 'can create new user.'
            response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
            return JsonResponse(response, safe=False)
    else:
        return HttpResponse("error method")