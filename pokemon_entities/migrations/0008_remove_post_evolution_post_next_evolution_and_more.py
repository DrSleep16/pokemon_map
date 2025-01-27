# Generated by Django 4.2.4 on 2023-08-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_remove_post_next_evolution_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='evolution',
        ),
        migrations.AddField(
            model_name='post',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolutions', to='pokemon_entities.post', verbose_name='Следующая эволюция'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.post', verbose_name='Предыдущая эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=None, verbose_name='Появление'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(default=None, verbose_name='Атака'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(default=None, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=None, verbose_name='Исчезновение'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=None, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=None, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.post', verbose_name='Покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=None, verbose_name='Стамина'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='eng_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Английское имя'),
        ),
        migrations.AlterField(
            model_name='post',
            name='jap_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Японское имя'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='pokemons_images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
    ]
