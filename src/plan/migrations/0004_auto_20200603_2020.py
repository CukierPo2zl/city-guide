# Generated by Django 2.2 on 2020-06-03 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20200603_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='route',
            field=models.ManyToManyField(to='ordered_attraction.OrderedAttraction'),
        ),
    ]
