# Generated by Django 2.0.2 on 2018-02-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='BlogApp.Tag', verbose_name='标签集合'),
        ),
    ]
