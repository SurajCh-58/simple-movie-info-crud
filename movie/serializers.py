from rest_framework import serializers
from movie.models import movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=movie
        fields=['id','title','genre','budget']