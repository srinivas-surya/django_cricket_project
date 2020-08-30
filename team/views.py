from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Team, Player, Matches, Points
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.shortcuts import get_object_or_404

# Create your views here.


def homepage(request):
    return render(request, "team/home.html", context=None)


def team_list(request):
    teaam_data = Team.objects.all()
    return render(request, "team/team_list.html", {"team_data": teaam_data})


def player_view(request, iden):
    player_list = Player.objects.filter(team_id=iden)
    return render(request, "team/player_list.html", {"player_list": player_list, "team_name": iden})


@csrf_exempt
def matches(request):
    if request.method == "POST":

        team1 = request.POST['team1']
        team2 = request.POST['team2']
        winner = request.POST["winner"]

        date_time = datetime.datetime.now()

        match_count = 0
        win_count = 0
        lose_count = 0
        points_count = 0

        if winner == team1 or winner == team2:
            """Insert data into matches tables"""
            data = Matches(team1=team1, team2=team2, winner=winner)
            data.save()
            if winner == team1:
                team1_obj = Points.objects.filter(team_name=team1)
                team2_obj = Points.objects.filter(team_name=team2)

                if team1_obj and team2_obj:

                    win_team_obj = Points.objects.get(team_name=team1)
                    lose_team_obj = Points.objects.get(team_name=team2)

                    """updating team1 data  into database"""
                    match_count = win_team_obj.matches_played + 1
                    win_count = win_team_obj.wins + 1
                    points_count = win_team_obj.points + 2

                    win_team_obj.matches_played = match_count
                    win_team_obj.wins = win_count
                    win_team_obj.points = points_count

                    win_team_obj.save()

                    match_count = 0

                    """updating team2 data into database"""
                    match_count = lose_team_obj.matches_played + 1
                    lose_count = lose_team_obj.lose + 1

                    lose_team_obj.matches_played = match_count
                    lose_team_obj.lose = lose_count

                    lose_team_obj.save()

                elif team1_obj and (team2_obj.count() == 0):

                    win_team_obj = Points.objects.get(team_name=team1)

                    """updating team1 data into database"""
                    match_count = win_team_obj.matches_played + 1
                    win_count = win_team_obj.wins + 1
                    points_count = win_team_obj.points + 2

                    win_team_obj.matches_played = match_count
                    win_team_obj.wins = win_count
                    win_team_obj.points = points_count

                    win_team_obj.save()

                    """updating team2 data into database"""
                    loser_point_data = Points(team_name=team2, matches_played=1, wins=0, lose=1, points=0)
                    loser_point_data.save()

                elif team1_obj.count() == 0 and team2_obj:

                    lose_team_obj = Points.objects.get(team_name=team2)

                    """updating team1 data into database"""
                    winner_point_data = Points(team_name=team1, matches_played=1, wins=1, lose=0, points=2)
                    winner_point_data.save()

                    """updating team2 data into database"""
                    match_count = lose_team_obj.matches_played + 1
                    lose_count = lose_team_obj.lose + 1

                    lose_team_obj.matches_played = match_count
                    lose_team_obj.lose = lose_count

                    lose_team_obj.save()

                else:
                    """updating team1 data into database"""
                    winner_team_data = Points(team_name=team1, matches_played=1, wins=1, lose=0, points=2)
                    winner_team_data.save()

                    """updating team2 data into database"""
                    loser_point_data = Points(team_name=team2, matches_played=1, wins=0, lose=1, points=0)
                    loser_point_data.save()

            elif winner == team2:

                team1_obj = Points.objects.filter(team_name=team1)
                team2_obj = Points.objects.filter(team_name=team2)

                if team1_obj and team2_obj:

                    win_team_obj = Points.objects.get(team_name=team2)
                    lose_team_obj = Points.objects.get(team_name=team1)

                    """updating team1 data  into database"""
                    match_count = win_team_obj.matches_played + 1
                    win_count = win_team_obj.wins + 1
                    points_count = win_team_obj.points + 2

                    win_team_obj.matches_played = match_count
                    win_team_obj.wins = win_count
                    win_team_obj.points = points_count

                    win_team_obj.save()

                    match_count = 0

                    """updating team2 data into database"""
                    match_count = lose_team_obj.matches_played + 1
                    lose_count = lose_team_obj.lose + 1

                    lose_team_obj.matches_played = match_count
                    lose_team_obj.lose = lose_count

                    lose_team_obj.save()

                elif team2_obj and (team1_obj.count() == 0):

                    win_team_obj = Points.objects.get(team_name=team2)

                    """updating team1 data into database"""
                    match_count = win_team_obj.matches_played + 1
                    win_count = win_team_obj.wins + 1
                    points_count = win_team_obj.points + 2

                    win_team_obj.matches_played = match_count
                    win_team_obj.wins = win_count
                    win_team_obj.points = points_count

                    win_team_obj.save()

                    """updating team2 data into database"""
                    loser_point_data = Points(team_name=team1, matches_played=1, wins=0, lose=1, points=0)
                    loser_point_data.save()

                elif team2_obj.count() == 0 and team1_obj:

                    lose_team_obj = Points.objects.get(team_name=team1)

                    """updating team1 data into database"""
                    winner_point_data = Points(team_name=team2, matches_played=1, wins=1, lose=0, points=2)
                    winner_point_data.save()

                    """updating team2 data into database"""
                    match_count = lose_team_obj.matches_played + 1
                    lose_count = lose_team_obj.lose + 1

                    lose_team_obj.matches_played = match_count
                    lose_team_obj.lose = lose_count

                    lose_team_obj.save()

                else:
                    """updating team1 data into database"""
                    winner_team_data = Points(team_name=team2, matches_played=1, wins=1, lose=0, points=2)
                    winner_team_data.save()

                    """updating team2 data into database"""
                    loser_point_data = Points(team_name=team1, matches_played=1, wins=0, lose=1, points=0)
                    loser_point_data.save()

            return HttpResponse("Data Stored Successfully")

        else:
            return HttpResponse("Please select the correct winner")

    else:
        data = Team.objects.all()
        return render(request, 'team/matches.html', {'team_data': data})


def points_table(request):

    points = Points.objects.all()

    return render(request, 'team/points.html', {'points': points})
