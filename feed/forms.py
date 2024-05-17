from django.forms import ModelForm
from django import forms
from .models import CV

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    
class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['title', 'pdf']
    
