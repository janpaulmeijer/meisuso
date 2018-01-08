# Generated by Django 2.0.1 on 2018-01-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userprofile_shirt_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('F', 'Fruit'), ('V', 'Vegetable')], default='', max_length=1),
        ),
    ]
