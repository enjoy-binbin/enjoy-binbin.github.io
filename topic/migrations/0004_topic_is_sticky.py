# Generated by Django 2.1 on 2019-04-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_comments_thank_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_sticky',
            field=models.BooleanField(default=0, verbose_name='是否置顶'),
        ),
    ]