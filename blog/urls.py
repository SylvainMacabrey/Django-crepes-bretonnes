from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('accueil', views.accueil, name="accueil"),
    path('article', views.createArticle, name='article.create'),
    path('article/<int:id>', views.lire, name='article.lire'),
    path('contact', views.contact, name='contact'),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="deconnexion")
]
