from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

from app01.models import Tblregistergroup,Tblcontestinfo
from utils.response import CommonResponseMixin, ReturnCode


def getAllGroupBrief(request):
    if(request.method=="GET"):
        ID=request.session.get("ID")
        print("id====",ID)
        data=Tblregistergroup.objects.filter(creatorid=ID).values('id','groupname','groupnumber','verifyflag','contestinfoid__name','schoolid__name','creatorid__name')
        for i in data:
            print(i)
        response=CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS,data=list(data))
        return JsonResponse(response,safe=False)
    pass


def getGroupInfoById(request):
    if(request.method == "GET"):
        id=request.GET.get("ID")
        data=Tblregistergroup.objects.filter(id=id).values('remark','workname','createdate','id','groupname','groupnumber'
                                                           ,'verifyflag','contestinfoid__name','schoolid__name','creatorid__name'
                                                           ,'score','offlineallocateid','offlinescore','offlinearrangescore'
                                                           ,'allscore','groupresult')
        response=CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS,data=list(data))
        return JsonResponse(response,safe=False)
    else:
        return HttpResponse("error")