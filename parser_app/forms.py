from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('manascinema.kg', 'manascinema.kg'),
        ('cinematica.kg', 'cinematica.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'manascinema.kg':
            film_parser = parser.parser()
            for i in film_parser:
                models.CinemaKg.objects.create(**i)

        if self.data['media_type'] == 'cinematica.kg':
            film_parser = parser.parser2()
            for i in film_parser:
                models.CinemaKg.objects.create(**i)
