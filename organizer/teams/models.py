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

    color_values=[
        "black",
        "grey",
        "darkgrey",
        "lightgrey",
        "white",
        "brown",
        "firebrick",
        "darkred",
        "salmon",
        "orangered",
        "chocolate",
        "darkorange",
        "moccasin",
        "orange",
        "goldenrod",
        "tan",
        "gold",
        "khaki",
        "beige",
        "olive",
        "yellow",
        "yellowgreen",
        "darkolivegreen",
        "lawngreen",
        "forestgreen",
        "limegreen",
        "green",
        "springgreen",
        "aquamarine",
        "turquoise",
        "teal",
        "cyan",
        "skyblue",
        "dodgerblue",
        "royalblue",
        "navy",
        "blue",
        "blueviolet",
        "indigo",
        "violet",
        "purple",
        "magenta",
        "deeppink",
        "crimson",
        "lightpink",
    ]

    colors_tuple = [(k,v.capitalize()) for k,v in zip(color_values,color_values)]

    primary_color = models.CharField(
        max_length=30, 
        default='black', 
        choices = colors_tuple
    )
    secondary_color = models.CharField(
        max_length=30, 
        default='black', 
        choices = colors_tuple
    )
    tertiary_color = models.CharField(
        max_length=30, 
        default='black', 
        choices = colors_tuple
    )

    # leagues = models.ManyToManyField(
    #     'events.TeamLeague', 
    #     related_name='teams'
    # )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)