from __future__ import unicode_literals

from django.db import models
from jxweb import config, data

# Create your models here.
class JXUser(models.Model):
    username = models.CharField(max_length=255, default='', null=False)
    password = models.CharField(max_length=255, default='', null=False)
    gender = models.CharField(max_length=1, choices=data.GENDER_CHOICES, default='', null=False)
    email = models.CharField(max_length=255, default='', null=False)
    phonenum = models.CharField(max_length=11, default='', null=False)
    
    firstname = models.CharField(max_length=255, default='', null=True)
    lastname = models.CharField(max_length=255, default='', null=True)
    icon = models.CharField(max_length=255, default='', null=True)
    description = models.TextField(default='', null=True)
    qq = models.CharField(max_length=12, default='', null=True)
    wechat = models.CharField(max_length=255, default='', null=True)
    city = models.CharField(max_length=255, default='', null=True)
    birthday = models.DateField(null=True)
    isblogger = models.BooleanField(null=False, default=False)
    isstaff = models.BooleanField(null=False, default=False)
    update_datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    create_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    removed = models.BooleanField(null=False, default=False)

    def getIcon(self):
        if self.icon:
            return self.icon
        else:
            return config.DEFAULT_USERICON

    def serializeForJson(self):
        icon = self.getIcon()

        jxuser = {
            "uid" : self.id,
            "username" : self.username,
            "gender" : self.gender,
            "email" : self.email,
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "icon" : icon,
            "qq" : self.qq,
            "wechat" : self.wechat,
            "city" : self.city,
            "birthday" : self.birthday,
            "isblogger" : self.isblogger,
            "isstaff" : self.isstaff,
        }
        return jxuser
