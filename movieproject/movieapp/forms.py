from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    #it means include the class with in class
    class Meta:
        model=Movie
        fields=['name','decs','year','img']
        