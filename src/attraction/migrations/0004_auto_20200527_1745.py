# Generated by Django 2.2 on 2020-05-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0003_auto_20200522_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.City'),
        ),
    ]
