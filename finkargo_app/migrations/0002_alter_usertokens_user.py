# Generated by Django 4.2.3 on 2023-07-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finkargo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertokens',
            name='user',
            field=models.CharField(default=True, max_length=23),
        ),
    ]
