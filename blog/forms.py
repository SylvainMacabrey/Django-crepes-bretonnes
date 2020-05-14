from django import forms
from .models import Article

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_sujet(self):
        sujet = self.cleaned_data['sujet']
        if "pizza" in sujet:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
        return sujet  # Ne pas oublier de renvoyer le contenu du champ traité

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
        return message  # Ne pas oublier de renvoyer le contenu du champ traité

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('date',)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)