from django.urls import path
from django.contrib import admin
from .views import IndexView, ReceitaPDFView


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('receitas/',ReceitaPDFView.as_view(), name='receita'),
]
