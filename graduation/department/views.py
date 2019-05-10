from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from app01 import models
from utils.response import ReturnCode, CommonResponseMixin


def getDepartmentList(request):
    if(request.method=="GET"):
        parentindex=request.GET.get("parentIndex")
        thelevel=request.GET.get("theLevel")

        data=models.Tbldepartmentinfo.objects.filter(parentindex=parentindex,thelevel=thelevel)\
            .values("id","name")
        listData=list(data)

        response={}
        response['data'] = listData
        response['result_code'] = ReturnCode.SUCCESS
        response['message'] = "get department list"
        return JsonResponse(data=response, safe=False)
    else:
        return HttpResponse("error")