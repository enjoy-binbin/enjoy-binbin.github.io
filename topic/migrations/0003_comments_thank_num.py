# Generated by Django 2.1 on 2019-04-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20190426_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='thank_num',
            field=models.IntegerField(default=0, verbose_name='感谢数'),
        ),
    ]
