# Generated by Django 4.1 on 2022-09-22 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_subscription_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='employee'),
        ),
    ]