# Generated by Django 3.0.2 on 2020-02-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesures', '0002_captureco2_capteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captureco2',
            name='capteur',
            field=models.CharField(blank=True, default='218', max_length=16, null=True),
        ),
    ]