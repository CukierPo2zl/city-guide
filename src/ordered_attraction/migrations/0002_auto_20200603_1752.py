# Generated by Django 2.2 on 2020-06-03 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordered_attraction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderedattraction',
            old_name='travle_length',
            new_name='travel_length',
        ),
    ]
