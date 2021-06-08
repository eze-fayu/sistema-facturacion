from django import forms
from .models import Categoria, SubCategoria
    
    
    
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion':"Descripción de la Categoria",
                "estado": "Estado"}
        widget = {"descripcion": forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            
class SubCategoriaForm(forms.ModelForm):
    # aca modifico para que si esta inactivo no lo muestre
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    # formulario para la subcategoria
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'descripcion':"SubCategoria",
                "estado": "Estado"}
        widget = {"descripcion": forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_table = "Seleccione Categoria"