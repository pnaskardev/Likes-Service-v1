# Generated by Django 4.2.4 on 2023-08-11 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_alter_quote_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='likes',
        ),
    ]
