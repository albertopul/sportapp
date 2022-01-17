# Generated by Django 3.2.8 on 2022-01-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20220103_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='sponsors',
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsor_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsor_2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsor_3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsor_4',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='sponsor_5',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
