import pytz
from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.core.validators import MaxLengthValidator, MinLengthValidator

COUNTRIES = [('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua & Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia & Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('VG', 'British Virgin Islands'), ('BN', 'Brunei'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'), ('BQ', 'Caribbean Netherlands'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo - Brazzaville'), ('CD', 'Congo - Kinshasa'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', 'Côte d’Ivoire'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard & McDonald Islands'), ('HN', 'Honduras'), ('HK', 'Hong Kong SAR China'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao SAR China'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar (Burma)'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('KP', 'North Korea'), ('MK', 'North Macedonia'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestinian Territories'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn Islands'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'São Tomé & Príncipe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia & South Sandwich Islands'), ('KR', 'South Korea'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('BL', 'St. Barthélemy'), ('SH', 'St. Helena'), ('KN', 'St. Kitts & Nevis'), ('LC', 'St. Lucia'), ('MF', 'St. Martin'), ('PM', 'St. Pierre & Miquelon'), ('VC', 'St. Vincent & Grenadines'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard & Jan Mayen'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad & Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks & Caicos Islands'), ('TV', 'Tuvalu'), ('UM', 'U.S. Outlying Islands'), ('VI', 'U.S. Virgin Islands'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('WF', 'Wallis & Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')]

class Driver(models.Model):
    class Meta:
        db_table='drivers'
        ordering=['name']
        indexes=[
            models.Index(fields=['user']),
            models.Index(fields=['name']),
        ]
        constraints=[
            models.UniqueConstraint(Lower('name'), name="unique_lower_driver_name"),

        ]
        #fields=["name", "region", "country", "device", "primary_color", "secondary_color", "tertiary_color"]
    
    user = models.OneToOneField(
        User, 
        on_delete=models.PROTECT,
        related_name='driver'
    )

    name = models.CharField(
        max_length=25,
        #default=User.get_username(),
        validators=[
            MinLengthValidator(3), 
            MaxLengthValidator(25)
        ],
        unique=True
    )

    teams = models.ManyToManyField(
        'teams.Team', 
        related_name='drivers'
    )

    leagues = models.ManyToManyField(
        'events.SingleLeague', 
        related_name='drivers'
    )

    region = models.CharField(
        max_length=20, 
        default='world', 
        choices=[
            ('na', 'North America'),
            ('sa', 'South America'),
            ('eu', 'Europe'),
            ('as', 'Asia'),
            ('af', 'Africa'),
            ('oc', 'Oceania'),
        ]
    )

    country = models.CharField(
        max_length=50,
        choices=COUNTRIES, 
        blank=True
    )

    timezone = models.CharField(
        max_length=30,
        default="UTC",
        choices=[(timezone,timezone) for timezone in pytz.common_timezones]
    )
    
    device = models.CharField(
        max_length=20, 
        default='controller', 
        choices = [
            ('controller', 'Controller'),
            ('keyboard', 'Keyboard'),
            ('both', 'Both'),
        ], 
        blank=True
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
