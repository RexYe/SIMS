# Generated by Django 2.0.4 on 2018-05-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0006_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('right_type', models.CharField(max_length=4)),
            ],
        ),
    ]