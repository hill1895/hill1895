# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hill1895', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category1',
            options={'ordering': ['-add_time']},
        ),
        migrations.AlterModelOptions(
            name='category2',
            options={'ordering': ['-add_time']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-add_time']},
        ),
        migrations.RenameField(
            model_name='category1',
            old_name='pub_time',
            new_name='add_time',
        ),
        migrations.RenameField(
            model_name='category2',
            old_name='pub_time',
            new_name='add_time',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='pub_time',
            new_name='add_time',
        ),
    ]
