from django.db import models

class Track(models.Model):
    name = models.CharField(
        max_length=100, 
        default='thunder_point_gp', 
        choices = [
            ('whistle_valley', 'Whistle Valley'),
            ('sugar_hill', 'Sugar Hill'),
            ('maple_ridge', 'Maple Ridge'),
            ('magdalena', 'Magdalena'),
            ('copperwood', 'Copperwood'),
            ('rennvoort', 'Rennvoort'),
            ('interstate', 'Interstate'),
            ('buffalo_hill', 'Buffalo Hill'),
            ('lost_lagoons', 'Lost Lagoons'),
            ('bullseye_speedway', 'Bullseye Speedway'),
            ('faenza', 'Faenza'),
            ('siena', 'Siena'),
            ('speedopolis', 'Speedopolis'),
            ('thunder_point', 'Thunder Point'),
            ('tilksport', 'Tilksport'),
        ], 
        unique=True
    )

    layout = models.CharField(
        max_length=20, 
        choices = [
            ('gp', 'GP'),
            ('club', 'Club'),
            ('mini', 'Mini'),
            ('oval', 'Oval'),
            ('rallycross', 'Rallycross'),
        ]
    )

    reversed = models.BooleanField(default=False)
    
    has_dirt = models.BooleanField(default=False)

    length_meters = models.FloatField()


class Car(models.Model):
    name = models.CharField(
        max_length=20, 
        default='road_rebel', 
        choices = [
            ('agitator', 'Agitator'),
            ('brusso', 'Brusso'),
            ('osprey', 'Osprey'),
            ('mantra', 'Mantra'),
            ('piccino', 'Piccino'),
            ('bonk', 'Bonk'),
            ('storm', 'Storm'),
            ('panther', 'Panther'),
            ('conquest', 'Conquest'),
            ('vost', 'Vost'),
            ('impact', 'Impact'),
            ('feather', 'Feather'),
            ('road_rebel', 'Road_rebel'),
            ('loose_cannon', 'Loose_cannon'),
        ], 
        unique=True
    )

    car_class = models.CharField(
        max_length=30, 
        default='touring_car', 
        choices = [
            ('super_truck', 'Super Truck'),
            ('50s_gt', '50s GT'),
            ('60s_gp', '60s GP'),
            ('80s_gp', '80s GP'),
            ('piccino_cup', 'Piccino Cup'),
            ('eurotruck', 'Eurotruck'),
            ('gp', 'GP'),
            ('gt', 'GT'),
            ('prototype', 'Prototpye'),
            ('rally', 'Rally'),
            ('stock_car', 'Stock Car'),
            ('superlights', 'Superlights'),
            ('touring_car', 'Touring Car'),
            ('muscle_car', 'Muscle Car'),
        ]
    )

    main_type = models.CharField(
        max_length=20, 
        default='street', 
        choices = [
            ('street', 'Street'),
            ('rallycross', 'Rallycross'),
        ]
    )

