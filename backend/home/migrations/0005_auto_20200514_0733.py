# Generated by Django 2.2.12 on 2020-05-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200514_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customtext',
            old_name='hjghfjgh',
            new_name='hghjg',
        ),
        migrations.AddField(
            model_name='customtext',
            name='jhgjgj',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='jhgjgjg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
