from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Название')
    photo = models.ImageField(upload_to='pokemons_images', null=True, verbose_name='Фото')
    description = models.TextField(default="", verbose_name='Описание')
    jap_name = models.CharField(max_length=200, blank=True, verbose_name='Японское имя')
    eng_name = models.CharField(max_length=200, blank=True, verbose_name='Английское имя')
    previous_evolution = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='next_evolutions', verbose_name='Предыдущая эволюция'
    )
    next_evolution = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='previous_evolutions', verbose_name='Следующая эволюция'
    )

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=None, verbose_name='Появление')
    disappeared_at = models.DateTimeField(default=None, verbose_name='Исчезновение')
    level = models.IntegerField(default=None, verbose_name='Уровень')
    health = models.IntegerField(default=None, verbose_name='Здоровье')
    attack = models.IntegerField(default=None, verbose_name='Атака')
    defense = models.IntegerField(default=None, verbose_name='Защита')
    stamina = models.IntegerField(default=None, verbose_name='Стамина')

    def __str__(self):
        return self.pokemon.title
