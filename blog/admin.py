from django.contrib import admin
from .models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):

    list_display   = ('titre', 'auteur', 'date')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    
    fieldsets = (
            # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu', )
        }),
)

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)