# Generated by Django 2.0.4 on 2018-05-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=30)),
                ('avatar_src', models.CharField(max_length=200)),
                ('work_experience', models.CharField(max_length=250)),
                ('edu_experience', models.CharField(max_length=250)),
                ('domain', models.CharField(max_length=60)),
                ('intro', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='paper_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abstract', models.CharField(max_length=600)),
                ('authors', models.CharField(max_length=100)),
                ('key_words', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('src', models.CharField(max_length=200)),
                ('authors_uniid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='paper_title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=100)),
                ('publish_time', models.CharField(max_length=30)),
                ('journal', models.CharField(max_length=50)),
                ('authors_uniid', models.CharField(max_length=200)),
            ],
        ),
    ]
