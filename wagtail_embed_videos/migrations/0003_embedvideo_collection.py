# coding: utf-8
# Generated by Django 1.10.5 on 2018-02-14 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_embed_videos', '0002_auto_20180822_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='embedvideo',
            name='collection',
            field=models.ForeignKey(default=wagtail.core.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtail.core.Collection', verbose_name='collection'),
        ),
    ]
