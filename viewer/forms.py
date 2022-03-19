from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, NumberInput, ModelForm

from viewer.models import Cars


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


def dupa_validator(value):
    if "dupa" in value.lower():
        raise ValidationError("Value contains restricted word.")


def unique_words_validator(value):
    word_list = value.strip('.').split(' ')
    if len(set(word_list)) != len(word_list):
        raise ValidationError("Description does not contain unique words.")


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Only past dates are allowed here.")


class CarForm(ModelForm):

    class Meta:
        model = Cars
        fields = '__all__'

    name = CharField(max_length=128, validators=[capitalized_validator])
    year_of_production = PastMonthField(widget=NumberInput(attrs={'type': 'date'}))
    description = CharField(widget=Textarea, required=False)


#
# class GenreForm(ModelForm):
#
#     class Meta:
#         model = Genre
#         fields = '__all__'
#
#     name = CharField(max_length=40)
