# Generated by Django 3.1.5 on 2021-12-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_auto_20211209_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='user_count',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
