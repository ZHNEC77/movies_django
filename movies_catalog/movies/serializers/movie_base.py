from movies_catalog.movies.models import Movie


from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "decription",
            "release_date",
            "duration",
            "age_rating",
        )
