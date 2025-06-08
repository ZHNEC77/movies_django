from django.contrib import admin

from movies.models import Movie, AgeRating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "decription",
        "release_date",
        "duration",
        "age_rating",
    )
    list_display_links = (
        "id",
        "title",
    )
    list_filter = (
        "title",
        "release_date",
        "age_rating",
    )
    search_fields = (
        "title",
        "decription",
    )


@admin.register(AgeRating)
class AgeRatindAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "decription",
    )
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = (
        "name",
        "decription",
    )
