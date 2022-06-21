from django.urls import path
from .views import pokemon_detail_view, pokemon_list_view


urlpatterns = [
    path("pokemon/", pokemon_list_view, name='pokemon-list-view'),
    path("pokemon/<int:poke_id>", pokemon_detail_view, name='pokemon-detail-view'),
]
