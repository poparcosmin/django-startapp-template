from django import forms

from .models import {{app_name|capfirst}}

class {{app_name|capfirst}}Form(forms.ModelForm):
    class Meta:
        model = {{app_name|capfirst}}
        fields = ["nume", "creat"]
        labels = {
            "nume": "Nume",
            "creat": "Adresă",
        }
