# Generated by Django 5.0.7 on 2024-07-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_sites_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]