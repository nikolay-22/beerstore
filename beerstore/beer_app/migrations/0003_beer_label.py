# Generated by Django 4.0.4 on 2022-04-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_app', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='label',
            field=models.ImageField(blank=True, upload_to='beerlabels/'),
        ),
    ]
