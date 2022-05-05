# Generated by Django 4.0.4 on 2022-05-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_location_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='image',
        ),
        migrations.AddField(
            model_name='animal',
            name='locationimage',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
