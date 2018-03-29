# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('start_time', models.DateField()),
                ('page_link', models.URLField()),
                ('image_link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('season', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200, choices=[(b'MAIN', b'main'), (b'SUPPORT', b'support')])),
                ('page_link', models.URLField()),
                ('image_link', models.URLField()),
                ('last_modified', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('anime', models.ForeignKey(to='seiyuu_mgr.Anime')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seiyuu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('page_link', models.URLField()),
                ('image_link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='character',
            name='seiyuu',
            field=models.ForeignKey(to='seiyuu_mgr.Seiyuu'),
            preserve_default=True,
        ),
    ]
