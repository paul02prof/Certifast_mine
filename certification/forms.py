from django import forms


class AddCertification(forms.Form):
    name = forms.CharField()
