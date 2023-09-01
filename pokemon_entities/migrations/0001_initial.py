# Generated by Django 4.2.4 on 2023-08-23 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(null=True, upload_to='pokemons_images')),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('appeared_at', models.DateTimeField(default=None)),
                ('disappeared_at', models.DateTimeField(default=None)),
                ('level', models.IntegerField(default=None)),
                ('health', models.IntegerField(default=None)),
                ('attack', models.IntegerField(default=None)),
                ('defense', models.IntegerField(default=None)),
                ('stamina', models.IntegerField(default=None)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.post')),
            ],
        ),
    ]
