# Generated by Django 3.0.2 on 2020-02-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0007_auto_20200226_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataproduct',
            name='systemproduct',
        ),
        migrations.AddField(
            model_name='dataproduct',
            name='table',
            field=models.CharField(blank=True, max_length=255, verbose_name='表名'),
        ),
        migrations.AddField(
            model_name='dataproduct',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='标题'),
        ),
    ]
