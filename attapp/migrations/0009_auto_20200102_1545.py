# Generated by Django 3.0 on 2020-01-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0008_assesment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sign',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='gender',
            new_name='Gender',
        ),
    ]