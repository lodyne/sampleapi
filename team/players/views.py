from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from team.players.models import Player
from team.players.serializers import PlayerSerializer

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, world. You're at the players index.")


def players_description(request):
    template_name = 'players/description.html'
    context = {
        'title': 'Players Description',
        'description': 'This is a description of the players.'
    }
    return render(request, template_name, context)


class PlayerListCreateView(ListCreateAPIView):
    """
    View to list and create players.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    


