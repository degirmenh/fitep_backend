# Generated by Django 3.1.5 on 2021-12-09 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
        ('account', '0002_coach_branches'),
        ('package', '0002_auto_20211209_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('currency', models.CharField(blank=True, choices=[('try', 'TRY'), ('usd', 'USD'), ('eur', 'EUR'), ('gbp', 'GBP')], max_length=3, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='branch.branch')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='account.coach')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'db_table': 'package',
            },
        ),
    ]
