from django import forms
from .models import Categoria, SubCategoria, Marca, Um, Productos
    
    
    
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        # campos que figuran en el formulario. tiene q estar si o si
        # este campo fields o exclude que pone todo menso lo q se pone ahi
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
        
        
class MarcaForm(forms.ModelForm):
    # aca modifico para que si esta inactivo no lo muestre
    # categoria = forms.ModelChoiceField(
    #     queryset=Categoria.objects.filter(estado=True)
    #     .order_by('descripcion')
    # )
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion':"Nombre de la Marca",
                "estado": "Estado"}
        widget = {"descripcion": forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            
            
class UmForm(forms.ModelForm):
    # aca modifico para que si esta inactivo no lo muestre
    # categoria = forms.ModelChoiceField(
        # queryset=Categoria.objects.filter(estado=True)
        # .order_by('descripcion')
    # )
    class Meta:
        model = Um
        fields = ['descripcion', 'estado']
        labels = {'descripcion':"Unidad de Medida",
                "estado": "Estado"}
        widget = {"descripcion": forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            
class ProductosForm(forms.ModelForm):
    # aca modifico para que si esta inactivo no lo muestre
    # categoria = forms.ModelChoiceField(
        # queryset=Categoria.objects.filter(estado=True)
        # .order_by('descripcion')
    # )

    class Meta:
        model = Productos
        fields = ['descripcion', 'estado', 'codigo', \
            'codigo_barra', 'precio', 'existencia', \
            'ultima_compra', 'marca', 'subcategoria', 'unidad_medida']
        labels = {'descripcion':"Producto",
                "estado": "Estado",
                'codigo': 'Código',
                'codigo_barra': 'Código de Barras',
                'precio': 'Precio',
                'existencia': 'Existencia',
                'ultima_compra':'Ultima Compra',
                'marca':'Marca',
                'subcategoria':'SubCategoria',
                'unidad_medida':'Unidad de Medida'
                }
        #  campos que quiero que se excluya
        exclude = ['um','fm','uc','fc']
        widget = {"descripcion": forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True