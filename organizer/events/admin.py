from django.contrib import admin

# Register your models here.
from .models import TeamLeague, SingleLeague, Race, RaceResults, Penalty

admin.site.register(TeamLeague)
admin.site.register(SingleLeague)
admin.site.register(Race)
admin.site.register(RaceResults)
admin.site.register(Penalty)