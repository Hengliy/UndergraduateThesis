from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse

from app01 import models
from utils.response import CommonResponseMixin, ReturnCode


def getDutyList(request):
    if(request.method=="GET"):
        data=models.Tbldutyinfo.objects.all().values()
        print(list(data))
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, data=list(data))
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse("error")

def index(request):

    user_list=models.Tbluserinfo.objects.all()

    for row in user_list:
        print(row.id,row.name)

    return render(request,'index.html',{"user_list":user_list})