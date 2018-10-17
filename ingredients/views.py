from django.shortcuts import render
from .models import Ingredient
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def ingredients_list(request):
    ingredients = Ingredient.objects.order_by()
    return render(request, 'html/ingredients_list.html', {'ingredients':ingredients})

def detail(request, ingredient_id):
    try:
        ingredient = Ingredient.objects.get(pk=ingredient_id)
    except Ingredient.DoesNotExist:
        raise Http404("ingredient does not exist")
    return render(request, 'html/detail.html', {'ingredient':ingredient})

def delete(request, ingredient_id):
    try:
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        ingredient.delete()
    except Ingredient.DoesNotExist:
        raise Http404("ingredient does not exist")
    return HttpResponseRedirect(reverse('ingredients:ingredients_list'))
def form (request):
    return  render(request,'html/add-ingredient.html')

def add (request):
    number=request.POST['artical_number']
    name=request.POST['name']
    amount=request.POST['amount']
    price=request.POST['price']
    unit=request.POST['group1']
    Ingredient(article_number=number,amount=amount,name=name,unit=unit,price=price).save()
    return HttpResponseRedirect(reverse('ingredients:ingredients_list'))


















# from django.shortcuts import render
# from django.views import generic
# from .models import Ingredient
#
# class IndexView(generic.ListView):
#   #template_name = 'html/index.html'
#   context_object_name = 'ingredient_list'
#   def get_queryset(self):
#     """Returns top 25 recipes sorted by total_calorie_count, descending; on tie, sort by name ascending"""
#     return Ingredient.objects.all().order_by('article_number')[:25]
#
#
#
# class UpdateIngredient(generic.):
#
#
#
# class DeleteIngredient():
#
# class AddIngredient():
#
#
#
#
#
# # Create your views here.
