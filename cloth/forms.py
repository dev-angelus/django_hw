from django import forms
from . import models


class ClothForm(forms.ModelForm):
    class Meta:
        model = models.OrderCL
        fields = "__all__"
        #fields = "title description"


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.OrderCL
        fields = "__all__"

