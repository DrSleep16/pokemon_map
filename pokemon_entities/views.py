import folium
from django.utils import timezone
from .models import PokemonEntity
from django.shortcuts import render, get_object_or_404


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
    pokemons_entities = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons_entities:
        image_url = request.build_absolute_uri(pokemon.pokemon.photo.url)
        add_pokemon(
            folium_map,
            pokemon.lat,
            pokemon.lon,
            image_url
        )

    pokemons_on_page = []
    for pokemon in pokemons_entities:
        image_url = request.build_absolute_uri(pokemon.pokemon.photo.url)
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
    requested_pokemon_entity = get_object_or_404(PokemonEntity, id=pokemon_id)
    image_url = request.build_absolute_uri(requested_pokemon_entity.pokemon.photo.url)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    next_evolution_data = None
    previous_evolution_data = None

    related_pokemon_entity = requested_pokemon_entity.pokemon.evolutions.first()
    if related_pokemon_entity:
        next_evolution_data = {
            'title_ru': related_pokemon_entity.title,
            'pokemon_id': related_pokemon_entity.id,
            'img_url': request.build_absolute_uri(related_pokemon_entity.photo.url),
        }

    evolution = requested_pokemon_entity.pokemon.previous_evolution
    if evolution:
        previous_evolution_data = {
            'title_ru': evolution.title,
            'pokemon_id': evolution.id,
            'img_url': request.build_absolute_uri(evolution.photo.url),
        }

    context = {
        'map': folium_map._repr_html_(),
        'pokemon': {
            'pokemon_id': requested_pokemon_entity.id,
            'img_url': image_url,
            'title_ru': requested_pokemon_entity.pokemon.title,
            'description': requested_pokemon_entity.pokemon.description,
            'title_en': requested_pokemon_entity.pokemon.eng_name,
            'title_jp': requested_pokemon_entity.pokemon.jap_name,
            'next_evolution': next_evolution_data,
            'previous_evolution': previous_evolution_data,
        }
    }

    return render(request, 'pokemon.html', context=context)
