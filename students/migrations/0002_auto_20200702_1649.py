# Generated by Django 2.2.12 on 2020-07-02 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Major',
            new_name='OfferedMajor',
        ),
    ]
