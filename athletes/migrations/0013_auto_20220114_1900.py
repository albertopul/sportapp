# Generated by Django 3.2.8 on 2022-01-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0012_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='sponsor_1',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='sponsor_2',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='sponsor_3',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='sponsor_4',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='sponsor_5',
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='athletes.Sponsor'),
        ),
    ]
