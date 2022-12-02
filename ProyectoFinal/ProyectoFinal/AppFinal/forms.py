from django import forms


class PostFormulario(forms.Form):
    post=forms.CharField(max_length=200)
    fecha_de_creacion=forms.DateField()

class AutorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)

class EstiloFormulario(forms.Form):
    estilo=forms.CharField(max_length=40)