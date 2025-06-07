from django.db import models


class AgeRating(models.Model):
    name = models.CharField(max_length=10, primary_key=True,)
    decription = models.TextField(blank=True, null=False,)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
