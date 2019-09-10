# Generated by Django 2.2.3 on 2019-09-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videogames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('year_release', models.IntegerField()),
            ],
        ),
    ]
