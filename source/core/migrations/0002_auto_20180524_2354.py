# Generated by Django 2.0.4 on 2018-05-24 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
