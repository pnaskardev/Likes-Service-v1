# Generated by Django 4.2.4 on 2023-08-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
