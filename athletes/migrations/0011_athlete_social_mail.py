# Generated by Django 3.2.8 on 2022-01-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0010_athlete_social_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='social_mail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
