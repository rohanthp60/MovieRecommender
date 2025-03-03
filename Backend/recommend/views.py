from django.shortcuts import render
from . import models
import requests



def home(request):
    return render(request, 'home.html')

def rec(request):
    movieName = request.GET['movie'].lower()

    if len(movieName) == 0:
        movieName = request.session.get('currentMovie', 'Avatar').lower()
    movieList = request.session.get(movieName, [])

    if len(movieList) > 0:
        searchedMovie = movieList[0][:2]
        Movies = [movieList[i][:2] for i in range(1, len(movieList))]
        return render(request, 'recommend.html', {'searchedMovie': searchedMovie, 'movies': Movies})
    
    dic = request.session.get('dictForMovie', {})

    try:
        movies = models.Movies.objects.get(key=movieName)
        movies = list(movies.get_values())
        Movies = []
        
        headers = {
            "accept": "application/json",
            "Authorization": "Own key"
        }

        m = movies[0]
        url = f"https://api.themoviedb.org/3/movie/{m}"
        response = requests.get(url=url, headers=headers)
        response = response.json()
        poster_path = response.get('poster_path', '')   
        movieList = [
            [response.get('title', 'Unknown Title'),
            f'https://image.tmdb.org/t/p/w200{poster_path}',
            response.get('tagline', ''),
            response.get('overview', ''),
            response.get('release_date', 'Not Released')]
        ]
        dic[response.get('title', '')] = movieList[-1]

        for i in range(1, len(movies)):
            m = movies[i]
            url = f"https://api.themoviedb.org/3/movie/{m}"
            response = requests.get(url=url, headers=headers)
            response = response.json()
            poster_path = response.get('poster_path', '')
            
            movieList.append([
                response.get('title', 'Unknown Title'),
                f'https://image.tmdb.org/t/p/w200{poster_path}',
                response.get('tagline', ''),
                response.get('overview', ''),
                response.get('release_date', 'Not Released')
            ])
            dic[response.get('title', '')] = movieList[-1]
        
        request.session[movieName] = movieList
        request.session['currentMovie'] = movieName
        request.session['dictForMovie'] = dic

        searchedMovie = movieList[0][:2]
        Movies = [movieList[i][:2] for i in range(1, len(movieList))]


        return render(request, 'recommend.html', {'searchedMovie': searchedMovie, 'movies': Movies})
    except Exception as e:

        print(f"Error: {e}")
        return render(request, 'recommend.html', {'searchedMovie': [f'{e}', ''], 'movies': []})


def spec(request):
    name = request.GET['movie_name']
    dictForMovie = request.session.get('dictForMovie', {})
    
    if name not in dictForMovie:
        return render(request, 'error.html', {'message': 'Movie not found'})
    
    data = dictForMovie[name]
    context = {
        'title': data[0],
        'imgPath': data[1],
        'tagline': data[2],
        'overview': data[3]
    }
    return render(request, 'specificMovie.html', context)

