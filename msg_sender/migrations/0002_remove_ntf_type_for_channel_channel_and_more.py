# Generated by Django 4.1 on 2022-09-20 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msg_sender', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ntf_type_for_channel',
            name='channel',
        ),
        migrations.AddField(
            model_name='ntf_type_for_channel',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='msg_sender.channel', verbose_name='channel'),
        ),
    ]