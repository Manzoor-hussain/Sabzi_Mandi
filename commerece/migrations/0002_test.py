# Generated by Django 2.1.5 on 2019-02-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerece', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=500)),
            ],
        ),
    ]