# Generated by Django 3.1.5 on 2021-12-09 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packagetype',
            options={'verbose_name': 'Package Type', 'verbose_name_plural': 'Package Types'},
        ),
        migrations.AlterModelTable(
            name='packagetype',
            table='package_type',
        ),
    ]
