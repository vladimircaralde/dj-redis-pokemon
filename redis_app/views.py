from django.shortcuts import render
from django.core.cache import cache

from .models import Pokemon


def pokemon_list_view(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'redis_app/pokemon/pokemon_list_view.html',
                  {"pokemons": pokemon})


def pokemon_detail_view(request, poke_id):
    if cache.get(poke_id):
        pokemon = cache.get(poke_id)                            # GET key
        message = 'hit the cache'
        count = cache.ttl(poke_id)                              # Time To Live
    else:
        try:
            pokemon = Pokemon.objects.get(id=poke_id)
            message = 'hit the db'
            count = ''
            cache.set(poke_id, pokemon, timeout=10)             # SET key  value
        except Pokemon.DoesNotExist:
            print('Pokemon does not exist')
            return

    return render(request, 'redis_app/pokemon/pokemon_detail_view.html',
                  {"pokemon": pokemon,
                   "message": message,
                   "count": count
                   })
