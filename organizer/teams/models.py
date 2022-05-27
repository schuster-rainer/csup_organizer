from django.db import models


class Team(models.Model):
    class Meta:
        db_table='teams'
        ordering=['name']
    
    name = models.CharField(max_length=40)
    tag = models.CharField(max_length=5)

    league = models.ManyToManyField(
        'events.TeamLeague', 
        on_delete=models.PROTECT,
        related_name='teams'
    )
