# Generated by Django 4.0 on 2021-12-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_project_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectImage',
            field=models.ImageField(upload_to='image/our_work'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=255),
        ),
    ]
