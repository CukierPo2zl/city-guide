# Generated by Django 2.2 on 2020-05-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0005_attraction_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='attractions/'),
        ),
    ]
