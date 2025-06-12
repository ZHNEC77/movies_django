from rest_framework import serializers
from movies.models import AgeRating
from movies.serializers.age_rating_base import AgeRatingSerializer
from movies.serializers.movie_base import MovieSerializer


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
