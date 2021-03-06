# Generated by Django 2.0.6 on 2018-07-18 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0003_messagereplayinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_start', models.BooleanField(default=False, verbose_name='星标')),
                ('is_read', models.BooleanField(default=False, verbose_name='读取')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, '保留'), (2, '删除'), (3, '永久删除')])),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msu_message', to='message.MessageInfo', verbose_name='消息')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msu_user', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户接受消息表',
                'verbose_name_plural': '用户接受消息表',
            },
        ),
    ]
