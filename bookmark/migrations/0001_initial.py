# Generated by Django 2.2.6 on 2019-10-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=300)),
                ('url', models.URLField(verbose_name='site url')),
            ],
        ),
    ]
