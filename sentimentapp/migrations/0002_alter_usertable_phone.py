# Generated by Django 3.2.25 on 2024-03-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
