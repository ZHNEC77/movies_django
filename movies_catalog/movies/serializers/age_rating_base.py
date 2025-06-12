from movies_catalog.movies.models import AgeRating


from rest_framework import serializers


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = (
            "name",
            "decription",
        )
