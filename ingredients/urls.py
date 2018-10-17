from django.urls import path
from . import views
app_name = 'ingredients'

urlpatterns = [
    path('', views.ingredients_list, name='ingredients_list'),
    path('<int:ingredient_id>/', views.detail, name='detail'),
    path('delete/<int:ingredient_id>', views.delete, name='delete'),
    path('form/', views.form, name='form'),
    path('add/', views.add, name='add'),

]