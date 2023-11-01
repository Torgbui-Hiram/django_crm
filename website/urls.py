from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms', views.form, name='form'),
    path('remove/<todo_id>', views.delete_todo, name='remove'),
    path('add_todo', views.add_todo, name='new_todo'),
    path('update_todo/<todo_id>', views.edit_todo, name='edit_todo'),
    path('chart', views.chart_view, name='chart-view'),
    path('products', views.add_product, name='add-product'),
    path('management', views.add_managers, name='managers'),
    path('depart', views.add_department, name='department'),

]
