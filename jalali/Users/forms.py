from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def clean_national_code(self):
        national_code = self.cleaned_data.get("national_code")
        if len(national_code.strip()) != 10:
            self.add_error("national_code", "wrong national code.")
            raise forms.ValidationError("wrong national code.")
        return national_code
        
    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if len(full_name.strip().split(" ")) != 2 or full_name != full_name.title():
            self.add_error("full_name", "invalid name.")
            raise forms.ValidationError("invlid name.")
        return full_name
