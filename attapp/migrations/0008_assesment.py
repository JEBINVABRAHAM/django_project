# Generated by Django 3.0 on 2020-01-02 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0007_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='assesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assesmentno', models.IntegerField()),
                ('sub1', models.CharField(max_length=20)),
                ('sub2', models.CharField(max_length=20)),
                ('sub3', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attapp.student')),
            ],
        ),
    ]