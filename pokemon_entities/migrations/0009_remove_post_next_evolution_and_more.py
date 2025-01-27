# Generated by Django 4.2.4 on 2023-08-26 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_remove_post_evolution_post_next_evolution_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='next_evolution',
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous_evolution',
        ),
        migrations.AddField(
            model_name='post',
            name='evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_pokemon', to='pokemon_entities.post', verbose_name='Эволюция'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=None, verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=None, verbose_name='Время исчезновения'),
        ),
        migrations.AlterField(
            model_name='post',
            name='eng_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Английское название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='jap_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Японское название'),
        ),
    ]
