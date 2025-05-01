Technos : Django - TailwindCss - JS

# Installer pipenv pour gérer facilement les dépendances (en évitant les conflits de dépendances) 
pip install pipenv


# Créer et Activer l'environnement virtuel
pipenv shell


# Installation de Django
pipenv install Django


# Création projet et l'application
django-admin startproject crudproject .
python manage.py startapp crudapp


# Démarrer et Tester
python manage.py runserver


// APPROCHE TEMPLATE FIRST


# Installer l'application dans le fichier settings 'INSTALLED_APPS'
# Configurations des statics files && templates (settings.py)
# Inclure les distributeurs d'urls(niveau project)
# Inclure les urls (niveau application)
# Définir les fichiers statiques et templates


# Mise en place de l'UI
https://dribbble.com/shots/15696664-Minimalist-Dashboard-UI-UX-Design

# Installation de mysqlclient
pipenv install mysqlclient

# Mise en place (configuration settings.py) de la db
# Migrations

# Création superuser
  -  admincrud
  -  admin@gmail.com
  -  edacy!123

# Implémentation de la logique login
# https://docs.djangoproject.com/fr/5.2/topics/auth/default/#django.contrib.auth.login


# Implémentation de la logique inscription
# https://docs.djangoproject.com/fr/5.2/topics/forms/
# https://github.com/mamadou-adiouma/littlelemon


# Implémentation du model products
- Noms produits
- Couleurs
- Categorie
- Prix
- Date de création (auto)

# Personnalisation
https://docs.djangoproject.com/fr/5.2/ref/contrib/admin/#:~:text=display%20%3D%20%22-empty-%22


# Affichage produits
nom : Apple MacBook Pro 17"
colour: Silver
category: Laptop
prix : $2999,00

nom : Samsung Galaxy S21
colour: Phantom Gray
category: Smartphone
prix : $799,00

nom : Sony WH-1000XM4
colour: Black
category: Headphones
prix : $349,00

nom : Microsoft Surface Pro 7
colour: Platinum
category: Tablet
prix : $749,00

nom : Dell XPS 13
colour: Frost White
category: Laptop
prix : $999,00

nom : Apple iPad Pro 12.9"
colour: Space Gray
category: Tablet
prix : $1099,00

nom : Google Pixel 6
colour: Sorta Seafoam
category: Smartphone
prix : $599,00

nom : ASUS ROG Zephyrus G14
colour: Moonlight White
category: Gaming Laptop
prix : $1499,00

nom : Fitbit Charge 5
colour: Black/Graphite
category: Fitness Tracker
prix : $179,95

nom : Amazon Echo Dot (4th Gen)
colour: Charcoal
category: Smart Speaker
prix : $49,99


# Detail produit (singleproduct_byid)
# Suppresion
# Ajout
# Mise à Jour

Completed CRUD !