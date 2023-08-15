from django.urls import path

from . import views

urlpatterns = [
    #Main Movies
    path('', views.movies, name='movies'),

    #All Movies
    path('movies/', views.allMovies, name='allMovies'),

    #Movies
    path('movies/<int:movies_id>/', views.movieDetails, name='movieDetails'),

    #Search Bar Movies
    path('searchbar/', views.searchbar, name='searchbar'),

    #Actors
    path('actors/<int:castcrew_id>/', views.castcrewDetails, name='actorDetails'),

    #Search Bar Actors
    path('searchbar/actors/', views.searchbarActors, name='searchbarActors'),

    #Writers
    path('writers/<int:castcrew_id>/', views.castcrewDetails, name='writerDetails'),

    #Search Bar Writers
    path('searchbar/writers/', views.searchbarWriters, name='searchbarWriters'),

    #Directors
    path('directors/<int:castcrew_id>/', views.castcrewDetails, name='directorDetails'),

    #Search Bar Directors
    path('searchbar/directors/', views.searchbarDirectors, name='searchbarDirectors'),

    #Insert a movie
    path('insert/', views.insert_movies, name='formMovies'),

    #Insert a cast/crew member
    path('insert/castcrew/', views.insert_castcrew, name='formCastcrew')

]
