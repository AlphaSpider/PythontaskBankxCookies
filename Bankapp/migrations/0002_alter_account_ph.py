# Generated by Django 5.2 on 2025-04-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ph',
            field=models.CharField(max_length=10),
        ),
    ]
