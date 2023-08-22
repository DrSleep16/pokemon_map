from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='pokemons_images', null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()