# Generated by Django 2.0.4 on 2018-05-14 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0002_auto_20180512_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper_title',
            name='journal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='paper_title',
            name='publish_time',
            field=models.CharField(max_length=60),
        ),
    ]
