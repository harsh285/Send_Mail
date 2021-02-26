# Generated by Django 3.1.7 on 2021-02-25 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='information',
            name='Intrest',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='information',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
