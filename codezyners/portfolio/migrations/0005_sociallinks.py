# Generated by Django 3.2.9 on 2021-12-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20211203_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
            ],
        ),
    ]