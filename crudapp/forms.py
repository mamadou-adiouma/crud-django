from django import forms
from crudapp.models import Inscription, Products


class InscriptionForm(forms.ModelForm):
    classes = 'bg-gray-50 border border-gray-300 mb-5 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'
    pwd_classes = 'col-span-3 bg-gray-50 border border-gray-300 mb-5 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'

    username = forms.CharField(widget=forms.TextInput(attrs={'class':classes, 'placeholder':'Nom utilisateur'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':classes, 'placeholder':'Adresse Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':classes, 'placeholder':'Votre prénom'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':classes, 'placeholder':'Votre nom de famille'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': pwd_classes, 'placeholder':'Entrez votre mot de passe'}))

    class Meta:
        model = Inscription
        fields = "__all__"



class AddProductForm(forms.ModelForm):
    classes = 'bg-gray-50 border border-gray-300 mb-5 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'

    nom = forms.CharField(widget=forms.TextInput(attrs={'class':classes, 'placeholder':'Nom Produit'}))
    couleur = forms.CharField(widget=forms.TextInput(attrs={'class':classes, 'placeholder':'Sa couleur'}))
    categorie = forms.CharField(widget=forms.TextInput(attrs={'class':classes, 'placeholder':'De quelle catégorie ?'}))
    prix = forms.CharField(widget=forms.NumberInput(attrs={'class':classes, 'placeholder':'Son prix'}))

    class Meta:
        model = Products
        fields = "__all__"
