from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=128)
    phone = models.CharField(verbose_name='手机号码', max_length=11)
    address = models.CharField(verbose_name='地址', max_length=256)

    class Meta:
        db_table = 'user'
