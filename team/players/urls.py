from django.urls import path
from .views import PlayerListCreateView, hello_world, players_description



urlpatterns = [
    path("",hello_world, name="hello_world"),
    path("description", players_description, name="players_description"),
    path('players', PlayerListCreateView.as_view(), name='player-list')
]
