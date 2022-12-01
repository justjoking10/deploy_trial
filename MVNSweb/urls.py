from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='MVNS-index'),
    path('view', views.view, name='MVNS-view'),
    path('add', views.add_data, name='MVNS-add-data'),
    path('edit/<int:pk>', views.edit_data, name='MVNS-edit-data'),
]