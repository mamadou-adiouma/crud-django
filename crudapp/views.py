from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from crudapp.forms import InscriptionForm, AddProductForm
from crudapp.models import Products


# Create your views here.
def index(request):
    products = Products.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes connectés avec succés !")
            return redirect('index')
        else:
            messages.error(request, "Identifiants incorrects !", )
            return redirect('index')
    return render(request, 'index.html', {'products': products})

def login_view(request):
    return  render(request, 'index.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté avec succés !")
    return redirect('index')


def inscription_view(request):
    form = InscriptionForm()
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            form.save()
            messages.success(request, "Inscription reussie !")
            form = InscriptionForm()
            return redirect('login')
        else:
            messages.error(request, "Erreur d'inscription !")
    ctx = {'form': form}
    return render(request, 'inscription.html', ctx)


def singleproduct_view(request, id):
    if request.user.is_authenticated:
        productby_id = Products.objects.get(id=id)
        return render(request, 'single-product.html', {'produit': productby_id})
    else:
        messages.error(request, "Vous devez être connecté pour afficher un produit. !")
        return redirect('login')


def deleteproduct_view(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Products, id=id)
        product.delete()
        messages.success(request, "Produit supprimé avec succès.")
        return redirect('index')
    else:
        messages.error(request, "Vous devez être connecté pour supprimer un produit.")
        return redirect('login')


def add_product_view(request):
    if request.user.is_authenticated:
        form = AddProductForm()
        if request.method == 'POST':
            form = AddProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Produit ajouté avec succès !")
                form = AddProductForm()
                return redirect('index')
            else:
                messages.error(request, "Erreur lors de l'ajout du produit !")
        ctx = {'form': form}
        return render(request, 'add-product.html', ctx)
    messages.error(request, "Vous devez être connecté pour ajouter un produit.")
    return redirect('login')


def update_product_view(request, id):
    if request.user.is_authenticated:
        productby_id = Products.objects.get(id=id)
        form = AddProductForm(instance=productby_id)
        if request.method == 'POST':
            productby_id = Products.objects.get(id=id)
            form = AddProductForm(request.POST, instance=productby_id)
            if form.is_valid():
                form.save()
                messages.success(request, "Produit mis à jour avec succès !")
                return redirect('index')
            else:
                messages.error(request, "Erreur lors de la mise à jour du produit !")
                return redirect('update')
        return render(request, 'update.html', {'form': form})

    messages.error(request, "Vous devez être connecté pour mettre à jour un produit.")
    return redirect('login')
