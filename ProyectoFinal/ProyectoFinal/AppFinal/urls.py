from django.urls import path

from AppFinal import views

urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path("posts/", views.posts,name='Posts'),
    path("postsApi/", views.postsapi),
    path("autoresApi/", views.Autoresapi),
    path("estilosApi/", views.Estilossapi),
    path("autores/", views.autores,name='Autores'),
    path("estilos/", views.estilos,name='Estilos'),
    path('buscar/', views.buscar),
    path('buscarAutor/', views.buscarautor)

]
