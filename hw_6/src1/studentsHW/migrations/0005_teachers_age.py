# Generated by Django 2.2.14 on 2020-07-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsHW', '0004_remove_teachers_name_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
