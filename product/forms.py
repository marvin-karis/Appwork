from django import forms

from .models import product

class ProductForm(forms.ModelForm):
    class Meta:
        model = product 
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "class" : "new-class-name two",
                "id" : "id-for-textarea",
                "rows" :20,
                "cols": 60
            }
        )
    )
    price       = forms.DecimalField(initial=999.99)