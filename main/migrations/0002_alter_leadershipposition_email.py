# Generated by Django 5.1.4 on 2025-01-27 23:50

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadershipposition',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[main.models.validate_umich_email]),
        ),
    ]
