# Generated by Django 2.0.4 on 2018-05-27 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='contry',
            new_name='country',
        ),
    ]