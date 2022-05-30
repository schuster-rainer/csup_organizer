# Generated by Django 4.0.4 on 2022-05-29 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='leagues',
            field=models.ManyToManyField(related_name='drivers', to='events.singleleague'),
        ),
        migrations.AddField(
            model_name='driver',
            name='teams',
            field=models.ManyToManyField(related_name='drivers', to='teams.team'),
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='driver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='driver',
            index=models.Index(fields=['user'], name='drivers_user_id_79997b_idx'),
        ),
        migrations.AddIndex(
            model_name='driver',
            index=models.Index(fields=['name'], name='drivers_name_f4d688_idx'),
        ),
        migrations.AddConstraint(
            model_name='driver',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='unique_lower_driver_name'),
        ),
    ]