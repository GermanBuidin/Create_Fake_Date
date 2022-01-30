from django.urls import path

from .views import *

urlpatterns = [
    path('', user_login, name='home'),
    path('new_schema/', new_schema, name="schema"),
    path('data_schemas/', data_schemas),
    path('data_sets/', data_sets, name='sets'),
    path('logout/', user_logout, name="logout"),
    path('data_sets/edit/<int:id>/', edit_schema )
]