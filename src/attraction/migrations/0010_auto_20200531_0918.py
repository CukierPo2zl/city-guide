# Generated by Django 2.2 on 2020-05-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0009_auto_20200529_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='longitude',
            field=models.FloatField(),
        ),
    ]