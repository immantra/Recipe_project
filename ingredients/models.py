from django.db import models



class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    article_number = models.IntegerField(null=False,default="-1")
    amount = models.FloatField(default=0.0)
    unit_price = models.FloatField(default=0.0)
    unit = models.CharField(max_length=20, choices=(
        ('g', 'Grams'),
        ('kg', 'Kilograms'),
        ('l', 'Litres'),
        ('cl', 'Centiliter'),
    ))


    @property
    def get_unit_price(self):
        return float(self.price) / float(self.amount)

    def __str__(self):
        return self.name
# override the save function to make the calculated attribute unit_price saved in the DB
    def save(self, *args, **kwargs):
        self.unit_price=self.get_unit_price
        super(Ingredient, self).save(*args, **kwargs)


