# Generated by Django 2.1 on 2018-08-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180804_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(help_text='MM/DD/YYYY'),
        ),
    ]
