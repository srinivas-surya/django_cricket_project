from django.urls import path
from team.views import team_list, homepage,  player_view, matches, points_table

urlpatterns = [
    path('player_list/<str:iden>/', player_view, name="player_list"),
    path("", homepage, name="home"),
    path("team_list/", team_list, name="team_list"),
    path("matches/", matches, name="matches"),
    path('points/', points_table, name='points')
]