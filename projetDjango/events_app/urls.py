from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_index, name='event_index'),
    path('match_detail/<int:id>', views.event_detail, name='event_detail'),
    path('search_result', views.search, name="search"),

    # les pages par categorie :
    path('Botola_Pro_Matchs', views.botola_pro_matchs, name="botola_pro_matchs"),
    path('Botola_2_Matchs', views.botola_2_matchs, name="botola_2_matchs"),
    path('Amateur_League_Matchs', views.amateur_league_matchs, name="amateur_league_matchs"),
    path('Coup_de_Trone_Matchs', views.coup_de_trone_matchs, name="coup_de_trone_matchs"),
]