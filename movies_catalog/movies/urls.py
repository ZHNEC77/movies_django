from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies import views


app_name = "movies"

router = DefaultRouter()
router.register("movies", views.MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
