# Generated by Django 3.2 on 2021-05-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
