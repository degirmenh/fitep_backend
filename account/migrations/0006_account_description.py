# Generated by Django 3.1.5 on 2021-12-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(default='', max_length=1031),
            preserve_default=False,
        ),
    ]
