# Generated by Django 2.0.2 on 2018-02-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, help_text='可选，如若为空将摘取正文的前54个字符', max_length=150, null=True, verbose_name='摘要'),
        ),
    ]