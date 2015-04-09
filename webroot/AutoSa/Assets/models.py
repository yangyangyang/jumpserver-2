from django.db import models
from UserManage.models import User


class IDC(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class SERV_STATUS(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class SERV_SORT(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Assets(models.Model):
    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=30)
    sort = models.ForeignKey(SERV_SORT)
    ip = models.CharField(max_length=20)
    memsize = models.IntegerField(max_length=4)
    disknum = models.IntegerField(max_length=4)
    port = models.IntegerField(max_length=5)
    idc = models.ForeignKey(IDC)
    status = models.ForeignKey(SERV_STATUS)
    type = models.CharField(max_length=20)
    instance = models.CharField(max_length=20)
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '%d %s ' % (self.id,self.ip)


class AssetsUser(models.Model):
    uid = models.ForeignKey(User)
    aid = models.ForeignKey(Assets)


