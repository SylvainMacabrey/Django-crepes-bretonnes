from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from blog.models import Article, Categorie
from .forms import ContactForm, ArticleForm, ConnexionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def accueil(request):
    articles = Article.objects.all() 
    return render(request, 'blog/accueil.html', {'derniers_articles': articles, 'date': datetime.now()})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article}) 

@login_required
def createArticle(request):
    form = ArticleForm(request.POST or None, request.FILES) 
    if form.is_valid(): 
        form.date = str(datetime.now())
        form.save()
        envoi = True
    return render(request, 'blog/createArticle.html', locals())

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
        envoi = True
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect('accueil')
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'blog/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))