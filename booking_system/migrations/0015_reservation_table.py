# Generated by Django 3.2.16 on 2022-10-25 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0014_auto_20221025_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking_system.table'),
        ),
    ]
