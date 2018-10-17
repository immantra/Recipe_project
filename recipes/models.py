from django.db import models
from ingredients.models import Ingredient


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    total_price_count = models.FloatField(default=0.0)

    @property
    def calculate_total_price_count(self):
        total_price = 0
        if self.amounts.all():
            for Ringredient in self.amounts.all():
                total_price += Ringredient.price
        return total_price



    def save(self, *args, **kwargs):
        self.total_price_count = self.calculate_total_price_count
        super(Recipe, self).save(*args, **kwargs)

    __unicode__ = lambda self: self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='amounts',on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='used_by',on_delete=models.CASCADE)
    amount = models.FloatField()
    price = models.FloatField(default=0.0)

    unit = models.CharField(max_length=20, choices=(
        ('g', 'Grams'),
        ('kg', 'Kilograms'),
        ('l', 'Litres'),
        ('cl', 'Centiliter'),
    ))

    @property
    def calculate_price(self):
        ingredient_unit=self.ingredient.unit;
        if(ingredient_unit.__eq__(self.unit)):
            return self.ingredient.unit_price*self.amount
        elif(ingredient_unit.__eq__("g") and self.unit.__eq__("kg")):
            return self.ingredient.unit_price * self.amount * 1000
        elif (ingredient_unit.__eq__("kg") and self.unit.__eq__("g")):
            return self.ingredient.unit_price * self.amount / 1000
        elif (ingredient_unit.__eq__("l") and self.unit.__eq__("cl")):
            return self.ingredient.unit_price * self.amount / 100
        elif (ingredient_unit.__eq__("cl") and self.unit.__eq__("l")):
            return self.ingredient.unit_price * self.amount * 100
        else:
            return -1
    def save(self, *args, **kwargs):
        self.price = self.calculate_price
        super(RecipeIngredient, self).save(*args, **kwargs)

# Create your models here.
