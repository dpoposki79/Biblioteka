# Generated by Django 4.0.4 on 2022-05-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_clenovi_pozajmena_kniga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clenovi',
            name='Telefon',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='knigi',
            name='El_path',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
