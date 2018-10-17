from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import RecipeIngredient,Recipe,Ingredient



def index(request):
    return  render(request,'html/index.html')


def recipes_list(request):
  recipes = Recipe.objects.order_by()
  return render(request, 'html/recipes_list.html', {'recipes': recipes})

def detail(request, recipe_id):
  try:
    recipe = Recipe.objects.get(pk=recipe_id)
  except Recipe.DoesNotExist:
    raise Http404("repice does not exist")
  return render(request, 'html/detail.html', {'recipe': recipe})

def form(request):
  return render(request, 'html/add-recipe.html')



def add(request):
  n=len(request.POST.getlist('myValue[]'))
  name = request.POST['recipe_name']
  re = Recipe(name=name)
  re.save()
  i=0;
  while i<n:
    i=i+1
    try:
        ingredient = Ingredient.objects.get(name=request.POST.getlist('name[]'))
    except Ingredient.DoesNotExist:
        raise Http404("ingredient does not exist")
    RecipeIngredient(recipe=re,ingredient=ingredient, unit=request.POST.getlist('unit[]')[i], amount=request.POST.getlist('amount[]')[i]).save()
  re.save()
  return HttpResponseRedirect(reverse('recipes:recipes_list'))

