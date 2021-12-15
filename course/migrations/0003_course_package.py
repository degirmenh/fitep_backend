# Generated by Django 3.1.5 on 2021-12-15 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_package_user_count'),
        ('course', '0002_course_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='package', to='package.package'),
            preserve_default=False,
        ),
    ]