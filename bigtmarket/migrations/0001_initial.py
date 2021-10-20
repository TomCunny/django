# Generated by Django 3.2.8 on 2021-10-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bigtusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('pgp', models.CharField(max_length=1000, unique=True)),
                ('vendor', models.BooleanField()),
            ],
        ),
    ]
