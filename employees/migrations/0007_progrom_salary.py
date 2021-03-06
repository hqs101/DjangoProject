# Generated by Django 2.0.6 on 2018-07-30 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0006_auto_20180730_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='项目名称')),
                ('description', models.CharField(max_length=1000, verbose_name='项目描述')),
                ('key_skill', models.CharField(max_length=1000, verbose_name='技术要点')),
                ('start_time', models.DateField(verbose_name='开始日期')),
                ('end_time', models.DateField(blank=True, null=True, verbose_name='结束日期')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_level', models.FloatField(max_length=3, verbose_name='工资标准')),
                ('salary_proportion', models.FloatField(max_length=3, verbose_name='工资比例')),
                ('gross_salary', models.FloatField(max_length=3, verbose_name='应发工资')),
                ('actual_salary', models.FloatField(max_length=3, verbose_name='实发工资')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
