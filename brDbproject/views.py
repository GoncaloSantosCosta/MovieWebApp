from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import CastCrew, Movies, Reviews
from .forms import Insert_movies, Insert_castcrew

# Create your views here.
def movies(request):
    template = loader.get_template('brDbproject/movies.html')
    topRated = Movies.objects.order_by('-imdb_r')[0:5]
    oldestMovies = Movies.objects.order_by('year')[0:5]
    newestMovies = Movies.objects.order_by('-year')[0:5]
    longestMovies = Movies.objects.order_by('-duration')[0:5]
    shortestMovies = Movies.objects.order_by('duration')[0:5]
    numberMovies = Movies.objects.all().count()
    context = {'topmovies':topRated, 'oldmovies':oldestMovies, 'newmovies':newestMovies, 'longmovies':longestMovies, 'shortmovies':shortestMovies, 'nmovies':numberMovies}
    return HttpResponse(template.render(context, request))

def allMovies(request):
    template = loader.get_template('brDbproject/allMovies.html')
    items = Movies.objects.order_by('title')[0:]
    context = {'movies':items}
    return HttpResponse(template.render(context, request))

def movieDetails(request, movies_id):
    template = loader.get_template('brDbproject/movieDetails.html')
    try:
        myMovie = Movies.objects.get(pk=movies_id)
        myMovieDirectors = CastCrew.objects.filter(movies__id = movies_id, role = 'Director')
        myMovieWriters = CastCrew.objects.filter(movies__id = movies_id, role = 'Writer')
        myMovieActors = CastCrew.objects.filter(movies__id = movies_id, role = 'Actor')
        myReview = Reviews.objects.filter(movie__id = movies_id)
        context = {'movie' : myMovie, 'directors' : myMovieDirectors, 'writers' : myMovieWriters, 'actors' : myMovieActors, 'reviews' : myReview}
    except Movies.DoesNotExist:
        raise Http404("Movie does not exist")

    return HttpResponse(template.render(context, request))

def castcrewDetails(request, castcrew_id):
    template = loader.get_template('brDbproject/castcrewDetails.html')
    try:
        myCastCrew = CastCrew.objects.get(pk = castcrew_id)
        myCastCrewMovies = Movies.objects.filter(castcrews__id = castcrew_id)
        myCastCrewMoviesNum = Movies.objects.filter(castcrews__id = castcrew_id).count()
        context = {'movies' : myCastCrewMovies, 'castcrew' : myCastCrew, 'nummovies' : myCastCrewMoviesNum}
    except CastCrew.DoesNotExist:
        raise Http404("Person does not exist")

    return HttpResponse(template.render(context, request))

def searchbar(request):
    template = loader.get_template('brDbproject/searchbar.html')
    if request.method == 'GET':
        mySearch = request.GET.get('search')
        myResult = Movies.objects.all().filter(title__icontains=mySearch)
        context = {'result' : myResult}
        return HttpResponse(template.render(context, request))

def searchbarActors(request):
    template = loader.get_template('brDbproject/searchbarActors.html')
    if request.method == 'GET':
        mySearch = request.GET.get('search')
        myResult = CastCrew.objects.all().filter(name__icontains=mySearch, role='Actor')
        context = {'result' : myResult}
        return HttpResponse(template.render(context, request))

def searchbarWriters(request):
    template = loader.get_template('brDbproject/searchbarWriters.html')
    if request.method == 'GET':
        mySearch = request.GET.get('search')
        myResult = CastCrew.objects.all().filter(name__icontains=mySearch, role='Writer')
        context = {'result' : myResult}
        return HttpResponse(template.render(context, request))

def searchbarDirectors(request):
    template = loader.get_template('brDbproject/searchbarDirectors.html')
    if request.method == 'GET':
        mySearch = request.GET.get('search')
        myResult = CastCrew.objects.all().filter(name__icontains=mySearch, role='Director')
        context = {'result' : myResult}
        return HttpResponse(template.render(context, request))

def insert_movies(request):
  if request.method == "POST":
    form = Insert_movies(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('movies'))
  else:
      form = Insert_movies()
  return render(request, 'brDbproject/insert-movie.html', {'form': form})

def insert_castcrew(request):
  if request.method == "POST":
    form = Insert_castcrew(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('formMovies'))
  else:
      form = Insert_castcrew()
  return render(request, 'brDbproject/insert-castcrew.html', {'form': form})
