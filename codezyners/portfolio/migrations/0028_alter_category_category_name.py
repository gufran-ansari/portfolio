# Generated by Django 4.1 on 2022-09-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0027_alter_clientreview_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('design', 'Graphic Design'), ('web-dev', 'Web Development')], max_length=255),
        ),
    ]
