# Generated by Django 2.0.4 on 2018-05-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0004_auto_20180514_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('introduction', models.CharField(max_length=800)),
                ('category', models.CharField(max_length=30)),
                ('logo', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('host_unit', models.CharField(max_length=100)),
                ('influence', models.CharField(max_length=20)),
                ('honor', models.CharField(max_length=50)),
            ],
        ),
    ]
