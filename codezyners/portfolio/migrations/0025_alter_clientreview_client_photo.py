# Generated by Django 4.0 on 2022-01-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_alter_clientreview_client_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='client_photo',
            field=models.ImageField(blank=True, default='image/index/user.jpg', null=True, upload_to=''),
        ),
    ]