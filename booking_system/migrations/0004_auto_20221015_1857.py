# Generated by Django 3.2.16 on 2022-10-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_alter_foodmenu_food_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmenu',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='foodmenu',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
