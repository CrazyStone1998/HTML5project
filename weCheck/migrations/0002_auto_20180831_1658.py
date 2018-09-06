# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weCheck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='effectiveDistance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='needFace',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='needLocation',
            field=models.BooleanField(default=False),
        ),
    ]
