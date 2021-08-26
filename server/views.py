from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from server import models
from server.models import Info


class Index(View):
    def get(self,request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        #l1 =LoginMsg(ipaddress=ip)
        #l1.save()
        return render(request,'index.html')

    def post(self,request):
        try:
            username = request.POST.get('username','')
            sapno = request.POST.get('sapno','')
            branch = request.POST.get('branch','')
            serno = request.POST.get('serno','')
            fundno = request.POST.get('fundno','')
            ipaddress = request.POST.get('ipaddress','')
            mac = request.POST.get('mac','')
            place = request.POST.get('place','')
            sys = request.POST.get('sys','')
            hostname = request.POST.get('hostname','')
            cpuinfo = request.POST.get('cpuinfo','')
            ccmprocess = request.POST.get('ccmprocess','')
            info = Info(username=username,sapno=sapno,branch=branch,serno=serno,fundno=fundno,place=place,ipaddress=ipaddress,mac=mac,sys=sys,hostname=hostname,cpuinfo=cpuinfo,ccmprocess=ccmprocess)
            info.save()
            #print(username)

            return HttpResponse('成功发送')
        except Exception as e:
            print(e)
            return HttpResponse('发送失败')


class Query(View):

    def get(self, request):
        return render(request, 'query.html')

    def post(self,request):
        branch = request.POST.get('branch', '')


        if branch !='':
            msg = models.Info.objects.filter(branch=branch)

        print(msg)
        return render(request, 'show.html', {'result': msg})
