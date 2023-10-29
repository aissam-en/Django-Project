from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Events

# Create your views here.

# afficher touts les events
def event_index(request):
    events = Events.objects.all()
    return render(request, 'events_app/event_index.html', {'events':events})


# afficher les details d'un event
def event_detail(request, id):
    detail = Events.objects.get(id = id)
    return render(request, 'events_app/event_detail.html', {'detail':detail})


# chercher un event
def search(request):
    if request.method == 'POST':
        search_bar_val = request.POST['search_bar']
        matchs = Events.objects.filter(match__contains=search_bar_val)
        return render(request, "events_app/search_result.html", {'search_bar_val':search_bar_val, 'matchs':matchs})
    else:
        return render(request, "events_app/search_result.html")


# afficher les events by categories
def botola_pro_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie = 'Botola PRO')
    return render(request, "events_app/by_category.html", {'matchs_list':matchs_list})
def botola_2_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie = 'Botola 2')
    return render(request, "events_app/by_category.html", {'matchs_list':matchs_list})
def coup_de_trone_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie = 'Coupe du Trone')
    return render(request, "events_app/by_category.html", {'matchs_list':matchs_list})
def amateur_league_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie = 'Amateur League')
    return render(request, "events_app/by_category.html", {'matchs_list':matchs_list})