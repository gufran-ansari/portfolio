# Generated by Django 4.0 on 2022-01-01 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_services_quotation_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]