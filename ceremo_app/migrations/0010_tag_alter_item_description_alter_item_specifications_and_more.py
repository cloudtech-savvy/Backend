# Generated by Django 5.0.3 on 2024-04-10 04:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceremo_app', '0009_remove_item_tags_item_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='This is a description of the Item  goes here .'),
        ),
        migrations.AlterField(
            model_name='item',
            name='specifications',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
