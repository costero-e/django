from django import forms

class PostForm(forms.Form):
    text = forms.CharField(label="Lugar")
    image = forms.FileField(label="Imagen")