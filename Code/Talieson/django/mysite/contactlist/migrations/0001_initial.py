# Generated by Django 3.0.6 on 2020-05-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('is_cell', models.BooleanField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
