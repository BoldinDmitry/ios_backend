# Generated by Django 3.1.3 on 2020-12-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0004_auto_20201227_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='edprogram',
            name='name',
            field=models.TextField(default='f'),
            preserve_default=False,
        ),
    ]
