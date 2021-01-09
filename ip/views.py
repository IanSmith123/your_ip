from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from .models import MyIP


def save_ip(request):
    # _ip = MyIP()
    _ip = request.GET.get("ip")
    _domain = request.GET.get("domain")

    my_ip = MyIP()
    sample = {"ip": _ip, "domain": _domain}
    my_ip.objects.create(sample)
    my_ip.save()

    r = dict()
    r['msg'] = "your ip saved"
    r['data'] = my_ip

    return JsonResponse(r, safe=False)


def query_ip(request):
    dic = dict()
    dic['a'] = 'b'

    return JsonResponse(dic, safe=False)
