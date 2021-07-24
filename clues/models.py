from django.db import models
from django.utils.text import slugify


class Publisher(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    slug = models.SlugField(null=False, blank=True, unique=True)
    url = models.CharField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Crossword(models.Model):
    published_on = models.DateField(null=False, blank=False)
    url = models.URLField(max_length=255, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  related_name="crosswords")

    def __str__(self):
        return f'{self.publisher.name} on {self.published_on}'


class Clue(models.Model):
    clue = models.CharField(null=False, blank=False, max_length=100)
    slug = models.SlugField(null=False, blank=True)
    answer = models.CharField(null=False, blank=False, max_length=30)
    crossword = models.ForeignKey(Crossword, on_delete=models.CASCADE,
                                  related_name="clues")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.clue)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.clue
