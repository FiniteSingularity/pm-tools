# Generated by Django 3.1.2 on 2020-10-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symbols', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='ticker',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
