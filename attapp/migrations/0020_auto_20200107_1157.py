# Generated by Django 3.0 on 2020-01-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0019_auto_20200107_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]