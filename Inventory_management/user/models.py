from django.db import models

# Create your models here.

# 관리자용 권한 설정
User_manager = (
    (0, 'Admin'),
    (1, 'User')
)

class User(models.Model):
    user_id = models.IntegerField(verbose_name='사번')
    name = models.CharField(max_length=10, verbose_name='이름')
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    auth = models.SmallIntegerField(choices=User_manager, verbose_name='권한설정')