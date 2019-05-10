from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from utils.response import CommonResponseMixin, ReturnCode
from django.views import View
from app01.models import Tblcontesttype
from app01.models import Tblcontestinfo

class ContestView(View, CommonResponseMixin):
    def get(self,requset):

        pass

    def post(self,request):

        pass

def getAllContestType(request):
    if (request.method == "GET"):
        data = Tblcontesttype.objects.filter(parentindex=-1).values()
        for i in data:
            data[i]=Tblcontestinfo.objects.filter(parentindex=i.id).values()


        print(list(data))
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, data=list(data))
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse("error")

def getAllContestInfo(request):
    if (request.method == "GET"):
        data = Tblcontestinfo.objects.all().values()
        print(list(data))
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, data=list(data))
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse("error")