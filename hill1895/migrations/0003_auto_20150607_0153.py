# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hill1895', '0002_auto_20150607_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category1',
            field=models.ForeignKey(verbose_name='\u4e00\u7ea7\u76ee\u5f55', to='hill1895.Category1'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category2',
            field=models.ForeignKey(verbose_name='\u4e8c\u7ea7\u76ee\u5f55', to='hill1895.Category2', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='hill1895.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
