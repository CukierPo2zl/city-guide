# Generated by Django 2.2 on 2020-05-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0004_auto_20200527_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='attractions/%Y/%m/%D/'),
        ),
    ]
