# Generated by Django 2.1.5 on 2019-02-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerece', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
