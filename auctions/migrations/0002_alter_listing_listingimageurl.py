# Generated by Django 4.0.5 on 2022-07-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='ListingImageUrl',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
