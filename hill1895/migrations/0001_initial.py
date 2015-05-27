# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('head_pic_url', models.URLField(null=True)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_1', models.CharField(unique=True, max_length=30, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_2', models.CharField(unique=True, max_length=30, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=30, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category1',
            field=models.ForeignKey(to='hill1895.Category1'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category2',
            field=models.ForeignKey(to='hill1895.Category2', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='hill1895.Tag', blank=True),
        ),
    ]
