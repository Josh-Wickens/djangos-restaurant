# Generated by Django 3.2.16 on 2022-10-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0009_alter_tables_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('number_of_people', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]