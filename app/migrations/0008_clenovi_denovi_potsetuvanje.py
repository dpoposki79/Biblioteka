# Generated by Django 4.0.4 on 2022-05-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_clenovi_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='clenovi',
            name='denovi_potsetuvanje',
            field=models.IntegerField(null=True),
        ),
    ]
