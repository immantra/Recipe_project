# Generated by Django 2.1.2 on 2018-10-16 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_total_price_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='instructions',
        ),
    ]
