# Generated by Django 2.2 on 2020-05-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0008_auto_20200529_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
