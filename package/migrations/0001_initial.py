# Generated by Django 3.1.5 on 2021-12-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField()),
                ('scale', models.CharField(blank=True, choices=[('hourly', 'Hourly'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'db_table': 'package',
            },
        ),
    ]
