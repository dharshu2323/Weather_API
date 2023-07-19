from django.forms import ModelForm,TextInput, Textarea
from .models import city

class cityform(ModelForm):
    class Meta:
        model=city
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'form-control','placeholder':'City name','id':'btn',})}