# Generated by Django 4.0.4 on 2022-05-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_clenovi_data_pozajmuvanje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clenovi',
            name='Telefon',
            field=models.CharField(max_length=20),
        ),
    ]
