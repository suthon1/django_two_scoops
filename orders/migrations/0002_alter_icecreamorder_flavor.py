# Generated by Django 4.1.7 on 2023-03-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecreamorder',
            name='flavor',
            field=models.CharField(choices=[('ch', 'chokolate'), ('vn', 'Vanilla'), ('st', 'Strawberry'), ('cm', 'chunky Munky')], max_length=2),
        ),
    ]
