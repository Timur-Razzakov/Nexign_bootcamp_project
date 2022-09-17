# Generated by Django 4.1 on 2022-09-17 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg_sender', '0002_notification_recipient_alter_result_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='channels',
        ),
        migrations.AddField(
            model_name='result',
            name='channels',
            field=models.ManyToManyField(to='msg_sender.channel', verbose_name='channels for send'),
        ),
    ]