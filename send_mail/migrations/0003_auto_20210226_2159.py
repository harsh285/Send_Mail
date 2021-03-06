# Generated by Django 3.1.7 on 2021-02-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0002_auto_20210225_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakeEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepient_email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='information',
            old_name='Intrest',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='address',
            new_name='Qty',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='name',
            new_name='product_name',
        ),
        migrations.AddField(
            model_name='information',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
