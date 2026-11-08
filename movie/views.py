from rest_framework import viewsets
from movie.serializers import MovieSerializer
from movie.models import movie

class MovieView(viewsets.ModelViewSet):
    queryset=movie.objects.all()
    serializer_class=MovieSerializer