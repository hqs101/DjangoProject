# Generated by Django 2.0.6 on 2018-07-19 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20180708_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interviewresume',
            options={'verbose_name': '人员简历', 'verbose_name_plural': '人员简历'},
        ),
        migrations.AddField(
            model_name='employee',
            name='enter_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='入职日期'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='leave_date',
            field=models.DateField(blank=True, null=True, verbose_name='离职日期'),
        ),
        migrations.AddField(
            model_name='employee',
            name='qualify_date',
            field=models.DateField(blank=True, null=True, verbose_name='转正日期'),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.IntegerField(choices=[(1, '已转正'), (2, '已离职'), (3, '试用期'), (4, '其他')], default=4, verbose_name='员工状态'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='type',
            field=models.IntegerField(choices=[(1, '正式员工'), (2, '实习生'), (3, '研究生'), (4, '培训生'), (5, '其他')], default=5, verbose_name='员工类型'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='bank_name',
            field=models.CharField(max_length=100, verbose_name='银行名称'),
        ),
        migrations.AlterField(
            model_name='card',
            name='branch_name',
            field=models.CharField(max_length=100, verbose_name='开户行'),
        ),
        migrations.AlterField(
            model_name='card',
            name='is_default',
            field=models.BooleanField(verbose_name='是否默认银行卡'),
        ),
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.CharField(max_length=100, verbose_name='银行卡号'),
        ),
        migrations.AlterField(
            model_name='card',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='银行预留手机号码'),
        ),
        migrations.AlterField(
            model_name='card',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='评价内容'),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='联系人姓名'),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='organization',
            field=models.CharField(max_length=1000, verbose_name='工作单位'),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='relationship',
            field=models.CharField(max_length=100, verbose_name='关系'),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='telephone',
            field=models.CharField(max_length=100, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='number',
            field=models.CharField(max_length=100, verbose_name='工号'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='idcard',
            name='id_card_address',
            field=models.CharField(max_length=100, verbose_name='身份证上的住址'),
        ),
        migrations.AlterField(
            model_name='idcard',
            name='id_card_number',
            field=models.CharField(max_length=18, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='idcard',
            name='id_card_photo',
            field=models.ImageField(upload_to='', verbose_name='身份证正反面扫描图'),
        ),
        migrations.AlterField(
            model_name='idcard',
            name='residence_address',
            field=models.CharField(max_length=1000, verbose_name='居住地'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='面试评语'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='interview_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='面试成绩'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='interviewer',
            field=models.CharField(max_length=100, verbose_name='面试官'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='result',
            field=models.TextField(blank=True, null=True, verbose_name='面试结果'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='time',
            field=models.DateTimeField(verbose_name='面试时间'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='应聘人'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='written_test_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='笔试成绩'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='english_level',
            field=models.IntegerField(choices=[(1, 'CET4'), (2, 'CET6'), (6, 'CET3'), (3, 'IELTS'), (4, 'TOEFL'), (5, '其他')], verbose_name='英语证书最高等级'),
        ),
    ]
