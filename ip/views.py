from django.shortcuts import render

import json
# Create your views here.
from django.http import HttpResponse, JsonResponse
from   django.shortcuts import render

from .models import MyIP


def save_ip(request):
    # _ip = MyIP()
    _ip = request.GET.get("ip")
    _domain = request.GET.get("domain")

    my_ip = MyIP()
    sample = {"ip": _ip, "domain": _domain}
    my_ip.ip = sample
    print(my_ip)
    my_ip.save()

    r = dict()
    r['msg'] = "your ip saved"
    r['data'] = sample

    return JsonResponse(r, safe=False)


def query_ip(request):
    dic = request.GET
    print("query: ", dic)
    # my_ip = MyIP.objects.filter(ip__ip=dic.get('ip'))
    # dic = {"ip__i'or'p": '1'}
    # my_ip = MyIP.objects.filter(**dic).all()
    # my_ip = MyIP.objects.filter(ip__domain=dic.get('domain')).all()
    my_ip = MyIP.objects.filter(ip__ip=dic.get('ip')).all()
    # my_ip = list(my_ip)
    print(my_ip)
    for i in my_ip:
        print(i)

    return JsonResponse(my_ip, safe=False)


def index(request):
    return render(request, 'index.html',)