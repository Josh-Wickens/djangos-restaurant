# Generated by Django 3.2.16 on 2022-10-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0005_foodmenu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodmenu',
            name='description',
            field=models.CharField(default='insert desciption', max_length=80),
        ),
        migrations.AlterField(
            model_name='foodmenu',
            name='food_type',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Mains', 'Mains'), ('Dessert', 'Dessert')], max_length=20),
        ),
    ]
