# Generated by Django 4.0.4 on 2022-05-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectCar', '0004_alter_contact_us_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
