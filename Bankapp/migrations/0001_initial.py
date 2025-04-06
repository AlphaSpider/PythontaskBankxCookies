# Generated by Django 5.2 on 2025-04-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('uname', models.CharField(max_length=100)),
                ('pswd', models.CharField(max_length=100)),
                ('adrs', models.CharField(max_length=250)),
                ('ph', models.IntegerField()),
                ('bal', models.FloatField()),
            ],
            options={
                'db_table': 'account_tbl',
            },
        ),
    ]
