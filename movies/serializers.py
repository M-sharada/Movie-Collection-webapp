from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Collection

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# Movie Serializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genres', 'uuid']

# Collection Serializer
class CollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Collection
        fields = ['title', 'description', 'movies']

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        collection = Collection.objects.create(**validated_data)
        for movie_data in movies_data:
            movie, created = Movie.objects.get_or_create(uuid=movie_data['uuid'], defaults=movie_data)
            collection.movies.add(movie)
        return collection
