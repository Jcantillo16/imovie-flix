from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializer import MovieSerializer
from apps.user.models import User


class MovieList(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieFilter(APIView):
    def get(self, request):
        category = request.GET.get('category')
        name = request.GET.get('name')
        premier_date = request.GET.get('premier_date')
        if category:
            movies = Movie.objects.filter(category__name=category)
        elif name:
            movies = Movie.objects.filter(name=name)
        elif premier_date:
            movies = Movie.objects.filter(premier_date=premier_date)
        else:
            movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# filrar unicamente por categoria
class MovieFilterCategory(APIView):
    def get(self, request):
        category = request.GET.get('category')
        movies = Movie.objects.filter(category__name=category)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# filrar unicamente por fecha
class MovieFilterDate(APIView):
    def get(self, request):
        premier_date = request.GET.get('premier_date')
        movies = Movie.objects.filter(premier_date=premier_date)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# filrar por categoria y nombre
class MovieFilterCategoryName(APIView):
    def get(self, request):
        category = request.GET.get('category')
        name = request.GET.get('name')
        movies = Movie.objects.filter(category__name=category, name=name)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# Order By  de la mas reciente a la mas antigua
class MovieFilterDateDesc(APIView):
    def get(self, request):
        movies = Movie.objects.all().order_by('-premier_date')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


#  peliculas de la A a la Z
class MovieFilterNameAsc(APIView):
    def get(self, request):
        movies = Movie.objects.all().order_by('name')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# peliculas nuevas
class MovieFilterNew(APIView):
    def get(self, request):
        movies = Movie.objects.filter(is_new=True)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# como usuario registrado deseo seleccionar una pelicula y verla.
class MovieFilterViewed(APIView):
    def get(self, request):
        movies = Movie.objects.filter(is_viewed=True)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    # ver pelicula y guardar el usuario que la vio
    def post(self, request, ):
        movie_id = request.data.get('movie_id')
        user_id = request.data.get('user_id')
        movie = Movie.objects.get(id=movie_id)
        movie.is_viewed = True
        user = User.objects.get(id=user_id)
        movie.view_by.add(user)
        movie.save()


        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
