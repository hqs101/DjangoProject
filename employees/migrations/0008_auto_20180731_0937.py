# Generated by Django 2.0.6 on 2018-07-31 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_progrom_salary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progrom',
            options={'verbose_name': '项目信息', 'verbose_name_plural': '项目信息'},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'verbose_name': '工资信息', 'verbose_name_plural': '工资信息'},
        ),
        migrations.RemoveField(
            model_name='progrom',
            name='user',
        ),
    ]
