# Generated by Django 5.0.1 on 2024-02-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='checkbox',
            field=models.BooleanField(default=False),
        ),
    ]