from django.db import models

# Create your models here.


class Team(models.Model):
    identifier = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    logoUri = models.ImageField(null=False)
    clubState = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)
        db_table = "Team"

    def __str__(self):

        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name="players")
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    imageUri = models.ImageField(null=False)
    playerJerseyNumber = models.IntegerField()
    country = models.CharField(max_length=15)

    class Meta:
        ordering = ('firstName',)
        db_table = "Player"

    def __str__(self):
        return self.firstName


class Matches(models.Model):
    team1 = models.CharField(max_length=20)
    team2 = models.CharField(max_length=20)
    winner = models.CharField(max_length=20)
    ccreated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('winner',)
        db_table = "Matches"

    def __str__(self):
        return self.winner


class Points(models.Model):
    team_name = models.CharField(max_length=20)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    lose = models.IntegerField()
    points = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('team_name',)
        db_table = "Points"


    def __str__(self):
        return self.team_name

