# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weCheck', '0002_auto_20180815_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(max_length=1000),
        ),
    ]
