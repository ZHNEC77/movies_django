from rest_framework import viewsets

from movies.models import Movie, AgeRating
from movies.serializers import MovieSerializer, AgeRatingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AgeRatingViewSet(viewsets.ModelViewSet):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer
