from django.shortcuts import render

# Create your views here.

from app01.models import Tbluserinfo

from django.http import HttpResponse, JsonResponse

from utils.response import CommonResponseMixin, ReturnCode


def login(request):

    if request.method == "POST":
        usericode = request.POST.get('usericode')
        passwd = request.POST.get('passwd')
        try:
            user = Tbluserinfo.objects.get(usericode=usericode)
            print('***************'+user.useripsd+'\n')
            if user.useripsd != passwd:
                response = CommonResponseMixin.wrap_json_response(code=ReturnCode.FAILED, message="密码错误")
                return JsonResponse(response, safe=False)

        except Tbluserinfo.DoesNotExist as e:
            response = CommonResponseMixin.wrap_json_response(code=ReturnCode.FAILED, message="用户不存在")
            return JsonResponse(response, safe=False)


        request.session['ID']=Tbluserinfo.objects.get(usericode=usericode).id
        request.session['is_authorized']=True
        request.session['message']='test Django session ok!'
        # 登录成功
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message="登陆成功")
        return JsonResponse(response, safe=False)

    else:
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.FAILED, message="请求错误")
        return JsonResponse(response, safe=False)

    # message = 'login successfully.'
    # response = wrap_json_response(data={}, code=ReturnCode.SUCCESS, message=message)
    # return JsonResponse(response, safe=False)


def register(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if not Tbluserinfo.objects.filter(name=username):
        new_user = Tbluserinfo(name=username,password=password)
        new_user.save()