# Generated by Django 2.1.2 on 2018-10-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_ingredient_article_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit_price',
            field=models.FloatField(default=0.0),
        ),
    ]