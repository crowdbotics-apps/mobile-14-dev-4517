# Generated by Django 2.2.12 on 2020-05-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200514_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='bbbgv',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='bgvhjv',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
