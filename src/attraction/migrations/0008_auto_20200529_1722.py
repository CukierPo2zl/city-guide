# Generated by Django 2.2 on 2020-05-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0007_auto_20200529_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='picture',
            field=models.ImageField(blank=True, height_field=320, null=True, upload_to='', width_field=240),
        ),
    ]
