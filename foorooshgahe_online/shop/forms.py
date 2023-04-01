import json

from django import forms

from shop.models import Product


class CartForm(forms.Form):    
    def __init__(self, *args, **kwargs):
        self.items:Product = kwargs.pop("items", [])
        super().__init__(*args, **kwargs)
        
        for i in self.items:
            self.fields[f"number_{i.id}"] = forms.IntegerField(
                initial=1,
                label=i.name,
                required=False
            )
            self.fields[f"color_{i.id}"] = forms.ChoiceField(
                choices=i.colors_available.values_list("name", "name"),
                required=False,
                initial=min(i.colors_available.order_by("name").first().name)
            )
            
    def clean(self):
        cleaned_data = super().clean()
        for i in self.items:
            if not cleaned_data.get(f"number_{i.id}", False):
                cleaned_data[f"number_{i.id}"] = 1
            if not cleaned_data.get(f"color_{i.id}", False):
                cleaned_data[f"color_{i.id}"] = i.colors_available.order_by("name").first().name
        return cleaned_data
