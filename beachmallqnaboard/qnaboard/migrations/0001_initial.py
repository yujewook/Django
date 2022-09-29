# Generated by Django 4.1 on 2022-09-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qnaboard',
            fields=[
                ('qnanum', models.AutoField(primary_key=True, serialize=False, verbose_name='글번호')),
                ('userid', models.CharField(max_length=20, verbose_name='작성자')),
                ('qnatitle', models.CharField(max_length=1000, verbose_name='글제목')),
                ('passwd', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('qnacontent', models.CharField(max_length=6000, verbose_name='글내용')),
                ('qnascore', models.IntegerField(default=0, verbose_name='조회수')),
                ('ref', models.IntegerField(verbose_name='그룹화 아이디')),
                ('restep', models.IntegerField(verbose_name='글순서')),
                ('relevel', models.IntegerField(verbose_name='글레벨')),
                ('qnadate', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('qnaip', models.CharField(max_length=15, verbose_name='아이피')),
                ('reply_order', models.CharField(max_length=15, verbose_name='댓글순서')),
                ('reply_depth', models.CharField(max_length=15, verbose_name='댓글깊이')),
                ('reply_number', models.CharField(max_length=15, verbose_name='댓글번호')),
                ('reply_title', models.CharField(max_length=1000, verbose_name='댓글제목')),
                ('reply_content', models.CharField(max_length=6000, verbose_name='관리자 댓글')),
            ],
        ),
    ]