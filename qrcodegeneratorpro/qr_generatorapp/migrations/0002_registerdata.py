# Generated by Django 4.2.7 on 2024-01-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_generatorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
