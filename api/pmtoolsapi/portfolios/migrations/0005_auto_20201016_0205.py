# Generated by Django 3.1.2 on 2020-10-16 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0004_auto_20201016_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelportfoliobench',
            old_name='portfolio_new',
            new_name='portfolio',
        ),
    ]
