# Generated by Django 3.0 on 2020-01-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0010_auto_20200102_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
