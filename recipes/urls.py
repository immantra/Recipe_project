from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes_list, name='recipes_list'),
    path('recipes/<int:recipe_id>/', views.detail, name='detail'),
    path('recipes/form/', views.form, name='form'),
    path('recipes/add/', views.add, name='add'),

]