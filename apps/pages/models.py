from django.contrib.auth.models import User
from django.db import models

class Contet(models.Model):
    author = models.ForeignKey(User, related_name='content', on_delete=models.CASCADE)
    title = models.CharField(max_length=180, unique=True, verbose_name='Titlu')
    text = models.TextField("Fulltext", max_length=10000000)
    users_like = models.ManyToManyField(User, related_name='contents_liked', blank=True)


    def __str__(self):
        return self.title

