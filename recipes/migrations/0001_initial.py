# Generated by Django 2.1.2 on 2018-10-15 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('unit', models.CharField(choices=[('g', 'Grams'), ('kg', 'Kilograms'), ('l', 'Litres'), ('cl', 'Centiliter')], max_length=20)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_by', to='ingredients.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amounts', to='recipes.Recipe')),
            ],
        ),
    ]
