from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ChoiceField, CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True):
        result = super(SignUpForm, self).save(commit)
        profile = Profile(id=result.id, biography='', gender='', user=result)
        if commit:
            profile.save()
        return result


class UserAccountUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class UserProfileUpdateForm(ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    class Meta:
        model = Profile
        fields = ['image', 'gender', 'biography']
        exclude = ['user']

    gender = ChoiceField(choices=GENDER_CHOICES, required=False)
    biography = CharField(label="Tell us about your car", widget=Textarea, required=False)
