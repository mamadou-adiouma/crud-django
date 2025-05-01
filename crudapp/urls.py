from django.urls import path
from crudapp import views


urlpatterns = [
    path('', views.index, name='index'),

    path('connexion/', views.login_view, name='login'),
    path('deconnexion/', views.logout_view, name='logout'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('produit/<int:id>/', views.singleproduct_view, name='produit'),
    path('supprimer-produit/<int:id>/', views.deleteproduct_view, name='supprimer-produit'),
    path('ajouter-produit/', views.add_product_view, name='ajouter-produit'),
    path('mettre-a-jour/<int:id>/', views.update_product_view, name='mettre-a-jour'),
]
