# Generated by Django 2.1.3 on 2018-12-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastName', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
    ]
