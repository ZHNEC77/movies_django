from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "decription",
        "release_date",
        "duration"
    )
    list_display_links = (
        "id",
        "title",
    )
    list_filter = (
        "title",
        "release_date",
    )
    search_fields = (
        "title",
        "decription",
    )
