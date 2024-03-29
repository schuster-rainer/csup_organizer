# Generated by Django 4.0.4 on 2022-06-01 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_remove_team_leagues_teamparticipation'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='primary_color',
            field=models.CharField(choices=[('black', 'Black'), ('grey', 'Grey'), ('darkgrey', 'Darkgrey'), ('lightgrey', 'Lightgrey'), ('white', 'White'), ('brown', 'Brown'), ('firebrick', 'Firebrick'), ('darkred', 'Darkred'), ('salmon', 'Salmon'), ('orangered', 'Orangered'), ('chocolate', 'Chocolate'), ('darkorange', 'Darkorange'), ('moccasin', 'Moccasin'), ('orange', 'Orange'), ('goldenrod', 'Goldenrod'), ('tan', 'Tan'), ('gold', 'Gold'), ('khaki', 'Khaki'), ('beige', 'Beige'), ('olive', 'Olive'), ('yellow', 'Yellow'), ('yellowgreen', 'Yellowgreen'), ('darkolivegreen', 'Darkolivegreen'), ('lawngreen', 'Lawngreen'), ('forestgreen', 'Forestgreen'), ('limegreen', 'Limegreen'), ('green', 'Green'), ('springgreen', 'Springgreen'), ('aquamarine', 'Aquamarine'), ('turquoise', 'Turquoise'), ('teal', 'Teal'), ('cyan', 'Cyan'), ('skyblue', 'Skyblue'), ('dodgerblue', 'Dodgerblue'), ('royalblue', 'Royalblue'), ('navy', 'Navy'), ('blue', 'Blue'), ('blueviolet', 'Blueviolet'), ('indigo', 'Indigo'), ('violet', 'Violet'), ('purple', 'Purple'), ('magenta', 'Magenta'), ('deeppink', 'Deeppink'), ('crimson', 'Crimson'), ('lightpink', 'Lightpink')], default='black', max_length=30),
        ),
        migrations.AddField(
            model_name='team',
            name='secondary_color',
            field=models.CharField(choices=[('black', 'Black'), ('grey', 'Grey'), ('darkgrey', 'Darkgrey'), ('lightgrey', 'Lightgrey'), ('white', 'White'), ('brown', 'Brown'), ('firebrick', 'Firebrick'), ('darkred', 'Darkred'), ('salmon', 'Salmon'), ('orangered', 'Orangered'), ('chocolate', 'Chocolate'), ('darkorange', 'Darkorange'), ('moccasin', 'Moccasin'), ('orange', 'Orange'), ('goldenrod', 'Goldenrod'), ('tan', 'Tan'), ('gold', 'Gold'), ('khaki', 'Khaki'), ('beige', 'Beige'), ('olive', 'Olive'), ('yellow', 'Yellow'), ('yellowgreen', 'Yellowgreen'), ('darkolivegreen', 'Darkolivegreen'), ('lawngreen', 'Lawngreen'), ('forestgreen', 'Forestgreen'), ('limegreen', 'Limegreen'), ('green', 'Green'), ('springgreen', 'Springgreen'), ('aquamarine', 'Aquamarine'), ('turquoise', 'Turquoise'), ('teal', 'Teal'), ('cyan', 'Cyan'), ('skyblue', 'Skyblue'), ('dodgerblue', 'Dodgerblue'), ('royalblue', 'Royalblue'), ('navy', 'Navy'), ('blue', 'Blue'), ('blueviolet', 'Blueviolet'), ('indigo', 'Indigo'), ('violet', 'Violet'), ('purple', 'Purple'), ('magenta', 'Magenta'), ('deeppink', 'Deeppink'), ('crimson', 'Crimson'), ('lightpink', 'Lightpink')], default='black', max_length=30),
        ),
        migrations.AddField(
            model_name='team',
            name='tertiary_color',
            field=models.CharField(choices=[('black', 'Black'), ('grey', 'Grey'), ('darkgrey', 'Darkgrey'), ('lightgrey', 'Lightgrey'), ('white', 'White'), ('brown', 'Brown'), ('firebrick', 'Firebrick'), ('darkred', 'Darkred'), ('salmon', 'Salmon'), ('orangered', 'Orangered'), ('chocolate', 'Chocolate'), ('darkorange', 'Darkorange'), ('moccasin', 'Moccasin'), ('orange', 'Orange'), ('goldenrod', 'Goldenrod'), ('tan', 'Tan'), ('gold', 'Gold'), ('khaki', 'Khaki'), ('beige', 'Beige'), ('olive', 'Olive'), ('yellow', 'Yellow'), ('yellowgreen', 'Yellowgreen'), ('darkolivegreen', 'Darkolivegreen'), ('lawngreen', 'Lawngreen'), ('forestgreen', 'Forestgreen'), ('limegreen', 'Limegreen'), ('green', 'Green'), ('springgreen', 'Springgreen'), ('aquamarine', 'Aquamarine'), ('turquoise', 'Turquoise'), ('teal', 'Teal'), ('cyan', 'Cyan'), ('skyblue', 'Skyblue'), ('dodgerblue', 'Dodgerblue'), ('royalblue', 'Royalblue'), ('navy', 'Navy'), ('blue', 'Blue'), ('blueviolet', 'Blueviolet'), ('indigo', 'Indigo'), ('violet', 'Violet'), ('purple', 'Purple'), ('magenta', 'Magenta'), ('deeppink', 'Deeppink'), ('crimson', 'Crimson'), ('lightpink', 'Lightpink')], default='black', max_length=30),
        ),
        migrations.AddField(
            model_name='team',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='teamparticipation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamparticipation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
