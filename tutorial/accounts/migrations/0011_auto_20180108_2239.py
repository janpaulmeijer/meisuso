# Generated by Django 2.0.1 on 2018-01-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180108_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='shirt_size',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('B', 'Buyer'), ('P', 'Producer'), ('O', 'Other')], default='', max_length=1),
        ),
    ]
