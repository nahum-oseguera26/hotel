from django import forms


class FormularioFiltroFactura(forms.Form):
    #aaa-mm-dd
    #2020-06-04
    fecha_incial = forms.charfield()
    fecha_incial = forms.charfield()
    