from django.db import models

# Create your models here.


class Info(models.Model):
    username = models.CharField(max_length=20)
    sapno = models.CharField(max_length=20)
    serno = models.CharField(max_length=50)
    fundno = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)
    ipaddress = models.CharField(max_length=20)
    hostname = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    sys = models.CharField(max_length=50)
    cpuinfo = models.CharField(max_length=50)
    ccmprocess = models.CharField(max_length=20)
    intime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'Info%s'%self.username
