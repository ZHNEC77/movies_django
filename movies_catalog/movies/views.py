from rest_framework import viewsets

from movies.models import Movie, AgeRating
from movies.serializers import MovieSerializer, AgeRatingSerializer, MovieSerializerExtend, MovieDetailSerializerExtend


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
    serializer_class = AgeRatingSerializer
