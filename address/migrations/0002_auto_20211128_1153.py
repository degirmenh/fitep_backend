# Generated by Django 3.1.5 on 2021-11-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
