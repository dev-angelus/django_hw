from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (VIPClient, "VIPClient"),
        (CLIENT, "Client")
    )

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHER, "OTHER")
    )

MARRIED = 1
SINGLE = 2
COMPLICATED = 3

MARITAL_STATUS = (
    (MARRIED, 'MARRIED'),
    (SINGLE, 'SINGLE'),
    (COMPLICATED, 'COMPLICATED')
)

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS)
    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'citizenship',
            'city',
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user