# Generated by Django 2.2.12 on 2020-06-09 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0006_auto_20200526_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumni', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
