import folium
import json
from django.utils import timezone
from .models import *
from django.http import HttpResponseNotFound
from django.shortcuts import render
from pogomap.settings import MEDIA_URL


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = timezone.now()
    pokemons = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        image_url = request.build_absolute_uri(MEDIA_URL + str(pokemon.pokemon.photo))
        add_pokemon(
            folium_map,
            pokemon.lat,
            pokemon.lon,
            image_url
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        image_url = request.build_absolute_uri(MEDIA_URL + str(pokemon.pokemon.photo))
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = PokemonEntity.objects.filter(id=pokemon_id)
    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            image_url = request.build_absolute_uri(MEDIA_URL + str(pokemon.pokemon.photo))
            break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map,
        requested_pokemon.lat,
        requested_pokemon.lon,
        image_url
    )
    pokemon_on_page = {
        'pokemon_id': pokemon.id,
        'img_url': image_url,
        'title_ru': pokemon.pokemon.title,
    }
    print(pokemon_on_page)
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })
