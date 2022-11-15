from django.db import models
from apps.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Movie(models.Model):
    name = models.CharField(max_length=100)
    premier_date = models.DateField(null=True, blank=True, default=None, auto_now=False,
                                    auto_now_add=False, verbose_name='premier date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies', null=False)
    is_new = models.BooleanField(default=False)
    img = models.CharField(max_length=500, null=False, default=None)
    view_by = models.ManyToManyField(User, related_name='movies_viewed', blank=True)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movies'
