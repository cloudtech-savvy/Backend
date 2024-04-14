# Generated by Django 5.0.3 on 2024-04-09 05:17

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceremo_app', '0008_alter_item_height_alter_item_length_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='tags',
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
