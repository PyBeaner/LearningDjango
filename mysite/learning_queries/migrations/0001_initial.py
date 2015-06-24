# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('mod_date', models.DateTimeField()),
                ('n_comments', models.IntegerField()),
                ('n_pingbacks', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('authors', models.ManyToManyField(to='learning_queries.Author')),
                ('blog', models.ForeignKey(to='learning_queries.Blog')),
            ],
        ),
    ]
