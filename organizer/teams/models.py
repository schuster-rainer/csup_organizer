from django.db import models
from django.db.models.functions import Lower
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Team(models.Model):
    class Meta:
        db_table='teams'
        ordering=['name']
        indexes=[
            models.Index(fields=['name']),
            models.Index(fields=['league']),
        ]
        constraints=[
            models.UniqueConstraint(Lower('name'), name="unique_lower_name"),
            models.UniqueConstraint(Lower('tag'), name="unique_lower_tag"),
        ]
    
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

    leagues = models.ManyToManyField(
        'events.TeamLeague', 
        on_delete=models.PROTECT,
        related_name='teams'
    )
