# Generated by Django 2.1.2 on 2018-10-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20181015_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
