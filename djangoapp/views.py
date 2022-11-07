import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from djangoapp.models import UserInfo


# Create your views here.
@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        name = UserInfo(name=request.GET.get('name'))
        password = UserInfo(password=request.GET.get('password'))
        name.save()
        password.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        user = UserInfo.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", user))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
