import folium
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
    try:
        requested_pokemon = PokemonEntity.objects.get(id=pokemon_id)
        image_url = request.build_absolute_uri(requested_pokemon.pokemon.photo.url)
    except PokemonEntity.DoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    # Создайте словари для следующей и предыдущей эволюции
    next_evolution_data = None
    previous_evolution_data = None

    if requested_pokemon.pokemon.next_evolution:
        next_evolution_data = {
            'title_ru': requested_pokemon.pokemon.next_evolution.title,
            'pokemon_id': requested_pokemon.pokemon.next_evolution.id,
            'img_url': request.build_absolute_uri(requested_pokemon.pokemon.next_evolution.photo.url),
        }

    if requested_pokemon.pokemon.previous_evolution:
        previous_evolution_data = {
            'title_ru': requested_pokemon.pokemon.previous_evolution.title,
            'pokemon_id': requested_pokemon.pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(requested_pokemon.pokemon.previous_evolution.photo.url),
        }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    context = {
        'map': folium_map._repr_html_(),
        'pokemon': {
            'pokemon_id': requested_pokemon.id,
            'img_url': image_url,
            'title_ru': requested_pokemon.pokemon.title,
            'description': requested_pokemon.pokemon.description,
            'title_en': requested_pokemon.pokemon.eng_name,
            'title_jp': requested_pokemon.pokemon.jap_name,
            'next_evolution': next_evolution_data,
            'previous_evolution': previous_evolution_data,
        }
    }

    return render(request, 'pokemon.html', context=context)
