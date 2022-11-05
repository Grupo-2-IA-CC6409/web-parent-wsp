from django import forms

from parentwsp.models import Session


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = (
            "name",
            "external_uuid",
        )
        widgets = {
            "external_uuid": forms.HiddenInput(),
        }
