# Generated by Django 2.0.2 on 2018-03-03 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ugrc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ugrc', models.CharField(max_length=200)),
                ('ugrc_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ugrc_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(max_length=10000000000)),
                ('ugrc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Ugrc')),
            ],
        ),
    ]
