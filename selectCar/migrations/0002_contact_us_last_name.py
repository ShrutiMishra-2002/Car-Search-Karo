# Generated by Django 4.0.4 on 2022-05-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectCar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='last_name',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
