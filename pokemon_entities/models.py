from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    photo = models.ImageField(
        upload_to='pokemons_images',
        verbose_name='Фото',
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    jap_name = models.CharField(
        max_length=200,
        verbose_name='Японское название',
        blank=True
    )
    eng_name = models.CharField(
        max_length=200,
        verbose_name='Английское название',
        blank=True
    )
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Эволюционировал из',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Post,
        verbose_name='Покемон',
        on_delete=models.CASCADE,
        related_name='entities'
    )
    lat = models.FloatField(
        verbose_name='Широта'
    )
    lon = models.FloatField(
        verbose_name='Долгота'
    )
    appeared_at = models.DateTimeField(
        verbose_name='Время появления'
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения'
    )
    level = models.IntegerField(
        verbose_name='Уровень'
    )
    health = models.IntegerField(
        verbose_name='Здоровье'
    )
    attack = models.IntegerField(
        verbose_name='Атака'
    )
    defense = models.IntegerField(
        verbose_name='Защита'
    )
    stamina = models.IntegerField(
        verbose_name='Стамина'
    )

    def __str__(self):
        return self.pokemon.title
