# Generated by Django 2.2.12 on 2020-07-30 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_alumnidata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnidata',
            name='conference_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='conference_location', to='account.Location'),
        ),
    ]
