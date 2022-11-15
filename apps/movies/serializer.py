from rest_framework import serializers
from .models import Movie, Category
from apps.user.models import User
import datetime


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['premier_date'] > datetime.date.today() - datetime.timedelta(weeks=3):
            validated_data['is_new'] = True
        return Movie.objects.create(**validated_data)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['view_by'] = instance.view_by.values_list('email', flat=True)
        response['category'] = instance.category.name
        return response
