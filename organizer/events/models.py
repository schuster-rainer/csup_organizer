import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.core.validators import MaxLengthValidator, MinLengthValidator, URLValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_time_format(input):
    import re
    p=re.compile("[0-9]{2,3}:[0-9]{2}.[0-9]{3}")

    if not p.match(input):
        raise ValidationError(
            _('%(input)s is not in the format 15:42.042!'),
            params={'input': input},
        )

class League(models.Model):
    class Meta:
        ordering = ['-created']
        constraints=[
            models.UniqueConstraint(Lower('name'), Lower('group'), 'season', name="unique_%(class)s_lower_name_group_season")
        ]
    
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(3), 
            MaxLengthValidator(50)
        ],
        help_text="Full name of the league without the group and season number, see below. Needs to be unique together with group and season."
    )

    abbreviation = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2), 
            MaxLengthValidator(10)
        ]
    )
    
    group = models.CharField(
        blank=True,
        max_length=50,
        validators=[
            MinLengthValidator(1), 
            MaxLengthValidator(50)
        ],
        help_text="Optional: Group"
    )
    season = models.PositiveSmallIntegerField(
        blank=True,
        validators=[MaxValueValidator(1000)],
        help_text="Optional: Season of the League"
    )

    website = models.CharField(
        max_length=500,
        validators=[
            MaxLengthValidator(500),
            URLValidator(schemes=['http', 'https'])
        ],
        blank=True,
        help_text="Optional: Wesbite of the League"
    )
    description = models.TextField(
        max_length=10000,
        validators=[
            MinLengthValidator(50), 
            MaxLengthValidator(10000)
        ],
    )
    previous_league_season = models.OneToOneField(
        'self',
        on_delete=models.DO_NOTHING,
        blank=True,
        related_name='next_league_season'
    )
    organizers = models.ManyToManyField(
        User, 
        related_name='leagues_organized',
        help_text="Choose who organizes this league. Those people can add races, enter results and edit the league."
    )

    region = models.CharField(
        max_length=20, 
        default='world', 
        choices = [
            ('world', 'World'),
            ('na', 'North America'),
            ('sa', 'South America'),
            ('na+sa', 'North and South America'),
            ('eu+na+sa', 'Europe, North and South America'),
            ('eu', 'Europe'),
        ]
    )
    
    # target_group = models.CharField(
    #     max_length=30, 
    #     default='experts', 
    #     choices = [
    #         ('experts', 'Expert Competition'),
    #         ('novice', 'Novice Competition'),
    #         ('fun', 'Fun Competition'),
    #     ]
    # )
    
    allocates_penalties = models.BooleanField(
        default=False,
        help_text="Are penalties allocated in this league, if someone drives unsportmanlikely?"
    )

    number_promotion = models.PositiveSmallIntegerField(
        blank=True,
        validators=[
            MaxLengthValidator(12)
        ],
        help_text="Optional: How many drivers will be promoted to higher group?"
    )

    number_demotion = models.PositiveSmallIntegerField(
        blank=True,
        validators=[
            MaxLengthValidator(12)
        ],
        help_text="Optional: How many drivers will be demoted to a lower group?"
    )
    
    points_p1 = models.PositiveSmallIntegerField(default=20)
    points_p2 = models.PositiveSmallIntegerField(default=16)
    points_p3 = models.PositiveSmallIntegerField(default=14)
    points_p4 = models.PositiveSmallIntegerField(default=12)
    points_p5 = models.PositiveSmallIntegerField(default=10)
    points_p6 = models.PositiveSmallIntegerField(default=8)
    points_p7 = models.PositiveSmallIntegerField(default=6)
    points_p8 = models.PositiveSmallIntegerField(default=5)
    points_p9 = models.PositiveSmallIntegerField(default=4)
    points_p10 = models.PositiveSmallIntegerField(default=3)
    points_p11 = models.PositiveSmallIntegerField(default=2)
    points_p12 = models.PositiveSmallIntegerField(default=1)

    points_pole = models.PositiveSmallIntegerField(default=1)
    points_fastest_lap = models.PositiveSmallIntegerField(default=1)

    points_for_attendance = models.BooleanField(
        default=False,
        help_text="Does someone get points, if he/she attended, but did not finish the quali/race? Quali finishers will go before those who dropped during Quali."
    )
    
    allow_registration_after_start = models.BooleanField(
        default=True,
        help_text="Can you still register after the first race?"
    )

    finished = models.BooleanField(
        default=False,
        help_text="Has the league been finished? Set this to True after the last race."
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TeamLeague(League):
    class Meta:
        db_table='team_leagues'
        # field=[
        #     "name","abbreviation","group","season","website","description","previous_league_season",
        #     "organizers", "region", "allocates_penalties",
        #     "points_p1","points_p2","points_p3","points_p4","points_p5","points_p6",
        #     "points_p7","points_p8","points_p9","points_p10","points_p11","points_p12",
        #     "points_pole","points_fastest_lap","points_for_attendance","participants_per_team",
        #     "number_promotion", "number_demotion", "allow_registration_after_start", "finished",
        #     "max_number_of_reserve_drivers","points_calculation_type", "finished"
        # ]
    
    participants_per_team = models.PositiveSmallIntegerField(
        default=2,
        validators=[
            MinLengthValidator(1), 
            MaxLengthValidator(12)
        ],
    )
    max_number_of_reserve_drivers = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinLengthValidator(0), 
            MaxLengthValidator(12)
        ],
    )
    
    points_calculation_type = models.CharField(
        max_length=30, 
        default='all', 
        choices = [
            ('all', 'Points of every race count'),
            ('cut_worst', 'Do not use worst team result'),
            ('cut_two_worst', 'Do not use the two worst team results'),
            ('use_best', 'Only use best team result per race'),
            ('use_two_best', 'Only use the two best team results per race'),
        ]
    )

class SingleLeague(League):  
    class Meta:
        db_table='single_leagues'
        # field=[
        #     "name","abbreviation","group","season","website","description","previous_league_season",
        #     "organizers", "region", "allocates_penalties",
        #     "points_p1","points_p2","points_p3","points_p4","points_p5","points_p6",
        #     "points_p7","points_p8","points_p9","points_p10","points_p11","points_p12",
        #     "points_pole","points_fastest_lap","points_for_attendance",
        #     "number_promotion", "number_demotion", "allow_registration_after_start", "finished",
        #     "points_calculation_type"
        # ]
    
    points_calculation_type = models.CharField(
        max_length=30, 
        default='all', 
        choices = [
            ('all', 'Points of every race count'),
            ('cut_worst', 'Do not use worst single/team result'),
            ('cut_two_worst', 'Do not use the two worst single/team results'),
        ]
    )

class Race(models.Model):
    class Meta:
        db_table='races'
        ordering=['league', 'datetime']
        indexes=[
            models.Index(fields=['league'])
        ]
        constraints=[
            models.UniqueConstraint(
                fields=['datetime','league'], 
                name="unique_%(class)s_lower_name_season"
            )
        ]
        # field=[
        #     "datetime","track","car",
        #     "quali_type","quali_duration_mode", "quali_duration", "quali_collisions",
        #     "race_duration_mode", "race_duration", "race_collisions",
        #     "drafting","rubberband","tire_wear","fuel_consumption",
        #     "damage_from_opponents","damage_from_environment"
        # ]
    
    datetime = models.DateTimeField()
    league = models.ForeignKey(
        League, 
        on_delete=models.PROTECT,
        related_name='races'
    )
    track = models.ForeignKey(
        'content.Track', 
        on_delete=models.PROTECT,
        related_name='races'
    )
    car = models.ForeignKey(
        'content.Car', 
        on_delete=models.PROTECT,
        related_name='races'
    )

    ### QUALI
    quali_type = models.CharField(
        max_length=20, 
        default='qualify', 
        choices = [
            ('qualify', 'Qualify'),
            ('no_qualifiers', 'No Qualifiers'),
            ('reverse_grid', 'Reverse Grid'),
        ]
    )
    quali_duration_mode = models.CharField(
        max_length=20, 
        default='laps', 
        choices = [
            ('laps', 'Laps'),
            ('distance', 'Distance (km)'),
            ('duration', 'Duration (minutes)'),
        ]
    )
    quali_duration = models.FloatField(default=1)
    
    quali_collisions = models.CharField(
        max_length=40, 
        default='prevent_all_collisions', 
        choices = [
            ('prevent_lapping_collisions', 'Prevent Lapping Collisions'),
            ('all', 'All'),
            ('prevent_all_collisions', 'Prevent All Collisions'),
        ]
    )

    ### RACE
    race_duration_mode = models.CharField(
        max_length=20, 
        default='laps', 
        choices = [
            ('laps', 'Laps'),
            ('distance', 'Distance'),
            ('duration', 'Duration (minutes)'),
        ]
    )
    race_duration = models.FloatField(default=15)
    
    race_collisions = models.CharField(
        max_length=40, 
        default='prevent_lapping_collisions', 
        choices = [
            ('prevent_lapping_collisions', 'Prevent Lapping Collisions'),
            ('all', 'All'),
            ('prevent_all_collisions', 'Prevent All Collisions'),
        ]
    )

    ### SETTINGS
    number_values = [0,25,50,75,100,125,150,175,200,250,300,350,400,450,500]
    number_values_tuple = [(k,str(v)) for k,v in zip(number_values,number_values)]
    validators=[MinLengthValidator(0), MaxLengthValidator(500)]
    
    drafting = models.PositiveSmallIntegerField(default=100, choices=number_values_tuple, validators=validators)
    rubberband = models.PositiveSmallIntegerField(default=0, choices=number_values_tuple, validators=validators)
    tire_wear = models.PositiveSmallIntegerField(default=100, choices=number_values_tuple, validators=validators)
    fuel_consumption = models.PositiveSmallIntegerField(default=100, choices=number_values_tuple, validators=validators)
    damage_from_opponents = models.PositiveSmallIntegerField(default=100, choices=number_values_tuple, validators=validators)
    damage_from_environment = models.PositiveSmallIntegerField(default=100, choices=number_values_tuple, validators=validators)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class RaceResults(models.Model):
    class Meta:
        db_table='race_results'
        ordering=['race', 'driver', '-attended_race', '-finished_race', 'race_position']
        indexes=[
            models.Index(fields=['race']),
            models.Index(fields=['driver'])
        ]
        # fields=[
        #     "driver","race","attended_quali","quali_position","quali_time_seconds"
        #     ,"attended_race","finished_race",
        #     "race_position","race_time_seconds","lappings","fastest_lap_seconds"
        # ]
    
    driver = models.ForeignKey(
        'drivers.Driver',
        on_delete=models.PROTECT,
        related_name='results'
    )
    race = models.ForeignKey(
        Race,
        on_delete=models.PROTECT,
        related_name='results'
    )

    attended_quali = models.BooleanField(blank=True)
    quali_position = models.PositiveSmallIntegerField(
        blank=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(12)]
    )
    quali_time_seconds = models.FloatField(
        blank=True,
        help_text="Please use the format 00:26.042",
        validators=[validate_time_format]
    )

    attended_race = models.BooleanField(default=True)
    finished_race = models.BooleanField(default=True)
    race_position = models.PositiveSmallIntegerField(
        blank=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(12)]
    )
    race_time_seconds = models.FloatField(
        blank=True,
        help_text="Please use the format 15:58.042",
        validators=[validate_time_format]
    )
    lappings = models.PositiveSmallIntegerField(
        blank=True,
        help_text="How often has the driver been lapped?"
    )
    fastest_lap_seconds = models.FloatField(
        blank=True,
        help_text="Please use the format 00:25.042",
        validators=[validate_time_format]
    )

class Penalty(models.Model):
    class Meta:
        db_table='penalties'
        order_with_respect_to='results'
        indexes=[
            models.Index(fields=['results'])
        ]
        # fields=[
        #     "type",
        #     "amount"
        # ]
    
    results = models.ForeignKey(
        RaceResults, 
        on_delete=models.CASCADE,
        related_name='penalties'
    )
    type = models.CharField(
        max_length=20, 
        default='time', 
        choices = [
            ('time', 'Time Penalty'),
            ('position', 'Position Penalty'),
        ]
    )
    number = models.FloatField(
        default=2,
        help_text="For time penalties use format '2.5' (for 2.5 seconds penalty), for positions use a simple digit."
    )
