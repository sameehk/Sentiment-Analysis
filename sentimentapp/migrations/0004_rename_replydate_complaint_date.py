# Generated by Django 3.2.25 on 2024-03-26 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentapp', '0003_complaint_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='replydate',
            new_name='date',
        ),
    ]
