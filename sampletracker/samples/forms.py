from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CellLine, Infection, CellExperiment


class CellExperimentForm(forms.ModelForm):
    class Meta:
        model = CellExperiment
        exclude = ["metadata", "created_at"]
