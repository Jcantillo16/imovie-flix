from rest_framework import serializers
from .models import User
from apps.movies.models import Movie
from apps.movies.serializer import MovieSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    movies_viewed = serializers.SerializerMethodField()

    def get_movies_viewed(self, obj):
        movies = Movie.objects.filter(view_by=obj.id)
        return MovieSerializer(movies, many=True).data
