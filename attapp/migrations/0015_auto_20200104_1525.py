# Generated by Django 3.0 on 2020-01-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0014_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='batchincharge',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
