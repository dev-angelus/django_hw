from django import forms
from . import models


class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = "__all__"
        #fields = "title description"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.CarReview
        fields = "__all__"

