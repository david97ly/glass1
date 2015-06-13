from django import forms
from django.forms import ModelForm
from models import *

class SlideForm(forms.Form):
    mensaje = forms.CharField(label='Mensaje Principal',max_length=100)
    submensaje = forms.CharField(label='Mensaje Secundario',max_length=100)
    

#class SlideForm(ModelForm):
 #   class Meta:
  #      model = Slide
       # exclude = ("votos","usuario")
