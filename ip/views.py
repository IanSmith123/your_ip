# author: Les1ie
# mail: me@les1ie.com

from django.shortcuts import render

import json
# Create your views here.
from django.http import HttpResponse, JsonResponse

from .models import MyIP


def save_ip(request):
    # _ip = MyIP()
    _ip = request.GET.get("ip")
    _domain = request.GET.get("domain")
    if _ip is None or _domain is None:
        return render(request, 'save.html')

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
    dic = dict(dic)
    if len(dic) == 0:
        return render(request, 'query.html')

    if not check_danger_string(json.dumps(dic)):
        msg = {'msg': "hacker"}
        return JsonResponse(msg)

    # good idea for all kind of query
    dic = {f"ip__{k}": dic[k][0] for k in dic}
    print(dic)
    my_ip = MyIP.objects.filter(**dic).all().values()
    my_ip = [item for item in my_ip]

    return JsonResponse(my_ip, safe=False)


def check_danger_string(s: str):
    ban_list = ['cmd', 'shell', 'exec', 'cyberpunk']
    for item in ban_list:
        if item in s:
            return False
    return True


def index(request):
    return render(request, 'index.html', )
