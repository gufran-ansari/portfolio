# Generated by Django 3.2.9 on 2021-12-05 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_sociallinks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialLinks',
            new_name='SocialLink',
        ),
    ]