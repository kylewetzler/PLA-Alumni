# Generated by Django 2.2.12 on 2020-05-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20200526_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='career_path',
            field=models.CharField(max_length=200),
        ),
    ]