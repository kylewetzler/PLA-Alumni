# Generated by Django 2.2.12 on 2020-07-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_studentorganization'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduationDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=6)),
                ('year', models.IntegerField()),
            ],
        ),
    ]