# Generated by Django 4.0 on 2022-01-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_rename_services_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='client_photo',
            field=models.ImageField(default='image/index/user.jpg', upload_to=''),
        ),
    ]
