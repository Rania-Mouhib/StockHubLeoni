from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="stockout"),
     path('add-stockout', views.add_stockout, name="add-stockout"),
]
