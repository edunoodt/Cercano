from django import forms
from . import models

class consulta_contacto_frm(forms.Form):
    apellido_contacto = forms.CharField(max_length=20,label='Apellido')

class consulta_producto_frm(forms.Form):
    nombre_producto = forms.CharField(max_length=20, label = 'Producto')