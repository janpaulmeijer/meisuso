# Generated by Django 2.0.1 on 2018-01-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20180108_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]