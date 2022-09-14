# Generated by Django 3.2.9 on 2021-12-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('Graphic Design', 'graphic'), ('Web Development', 'web')], max_length=255),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='service',
            field=models.CharField(choices=[('Graphic Design', 'graphic'), ('Web Development', 'web')], max_length=100),
        ),
    ]