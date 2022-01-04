# Generated by Django 3.1.5 on 2022-01-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20220104_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='education_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Primary'), (1, 'Secondary'), (2, 'High'), (3, 'College'), (4, 'Sport Academy'), (5, 'Bachelor'), (6, 'Master'), (7, 'Doctorate')], default=2),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'female'), (1, 'male')], default=2, null=True),
        ),
    ]
