# Generated by Django 3.1.5 on 2022-01-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20211224_2046'),
        ('package', '0007_package_user_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='coach',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='account.coach'),
        ),
    ]