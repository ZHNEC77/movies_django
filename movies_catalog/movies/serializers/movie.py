from rest_framework import serializers
from movies.models import Movie, AgeRating
from movies.serializers.age_rating import AgeRatingSerializer


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


class MovieSerializerExtend(serializers.HyperlinkedModelSerializer):
    age_rating = serializers.HyperlinkedRelatedField(
        view_name="movies:agerating-detail",
        queryset=AgeRating.objects.all(),
    )

    class Meta(MovieSerializer.Meta):
        pass


class MovieDetailSerializerExtend(MovieSerializer):
    age_rating = AgeRatingSerializer(
        many=False,
    )

    class Meta(MovieSerializer.Meta):
        pass
