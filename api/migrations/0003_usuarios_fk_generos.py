# Generated by Django 5.1.2 on 2024-10-15 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='fk_generos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.generos'),
        ),
    ]
