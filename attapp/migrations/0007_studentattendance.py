# Generated by Django 3.0 on 2020-01-02 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0006_auto_20200102_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentattendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status_hour1', models.CharField(max_length=10)),
                ('status_hour2', models.CharField(max_length=10)),
                ('status_hour3', models.CharField(max_length=10)),
                ('status_hour4', models.CharField(max_length=10)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attapp.student')),
            ],
        ),
    ]