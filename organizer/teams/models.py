from django.db import models
from django.db.models.functions import Lower
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Team(models.Model):
    class Meta:
        db_table='teams'
        ordering=['name']
        indexes=[
            models.Index(fields=['name']),
        ]
        constraints=[
            models.UniqueConstraint(Lower('name'), name="unique_lower_team_name"),
            models.UniqueConstraint(Lower('tag'), name="unique_lower_team_tag"),
        ]
        #fields=["name","tag"]
    
    name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(2), 
            MaxLengthValidator(40)
        ],
        unique=True
    )

    tag = models.CharField(
        max_length=5,
        validators=[
            MinLengthValidator(2), 
            MaxLengthValidator(5)
        ],
        unique=True
    )

    # leagues = models.ManyToManyField(
    #     'events.TeamLeague', 
    #     related_name='teams'
    # )

class TeamParticipation(models.Model):
    class Meta:
        db_table='team_participations'
    
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='participations'
    )

    league = models.ForeignKey(
        'events.League', 
        on_delete=models.CASCADE,
        related_name='team_participations'
    )

    drivers = models.ManyToManyField(
        'drivers.Driver',
        related_name='team_driver_participations'
    )

    reserve_drivers = models.ManyToManyField(
        'drivers.Driver',
        related_name='team_reserve_driver_participations'
    )