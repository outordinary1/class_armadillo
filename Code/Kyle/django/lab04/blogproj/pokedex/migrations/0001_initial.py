# Generated by Django 3.0.6 on 2020-06-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('image_front', models.CharField(max_length=200)),
                ('image_back', models.CharField(max_length=200)),
                ('types', models.ManyToManyField(to='pokedex.PokemonType')),
            ],
        ),
    ]
