from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Group(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название группы')
    slug = models.SlugField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )

    class Meta:
        ordering=['-pub_date']

