# Generated by Django 4.2.3 on 2023-07-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finkargo_app', '0008_remove_usertoken_begin_date_usertoken_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='create_date',
            field=models.CharField(null=True),
        ),
    ]
