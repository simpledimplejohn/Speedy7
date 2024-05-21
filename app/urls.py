from django.urls import path
from . import views
from .views import tomato_view

urlpatterns = [
    path("", views.index, name="index"),
    path('tomato/', tomato_view,name='tomato'),
    path('variables/', views.variables_view, name='variables'),
]
