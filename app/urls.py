from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('tomato/', views.tomato_view,name='tomato'),
    path('variables/', views.variables_view, name='variables'),
    path('new_variable/', views.new_variable, name='new_variable')
]

