# Generated by Django 3.0.2 on 2020-02-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_configdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configsrc',
            name='port',
            field=models.IntegerField(verbose_name='端口号'),
        ),
    ]
