from rest_framework import viewsets

from movies.models import Movie, AgeRating
from movies.serializers import MovieSerializerExtend, MovieDetailSerializerExtend
from movies.serializers.age_rating_base import AgeRatingSerializer
from movies.serializers.movie_base import MovieSerializer
from movies.serializers.age_rating import AgeRatingDetailSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        qs = self.queryset
        if self.action == "retrieve":
            qs = qs.select_related("age_rating")
            return MovieDetailSerializerExtend
        return qs

    def get_serializer_class(self):
        if self.request.GET.get("include"):
            if self.action == "retrieve":
                return MovieDetailSerializerExtend
            return MovieSerializerExtend
        return MovieSerializer


class AgeRatingViewSet(viewsets.ModelViewSet):
    queryset = AgeRating.objects.all()

    def get_queryset(self):
        qs = self.queryset
        if self.action == "retrieve":
            qs = qs.prefetch_related("movies")
        return qs

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AgeRatingDetailSerializer
        return AgeRatingSerializer
