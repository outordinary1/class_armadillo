# Generated by Django 3.0.6 on 2020-06-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]