# Generated by Django 3.0.6 on 2020-05-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20200526_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='completed_date',
            field=models.DateTimeField(verbose_name='date completed'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='publish_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]