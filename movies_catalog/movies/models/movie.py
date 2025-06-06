from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=120, db_index=True)
    decription = models.TextField(blank=True, null=False)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self) -> str:
        return self.title
