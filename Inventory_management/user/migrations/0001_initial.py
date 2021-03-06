# Generated by Django 3.1.6 on 2021-02-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='사번')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('auth', models.SmallIntegerField(choices=[(0, 'Admin'), (1, 'User')], verbose_name='권한설정')),
            ],
        ),
    ]
