# Generated by Django 2.2.12 on 2020-06-02 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20200602_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='conversation',
        ),
    ]
