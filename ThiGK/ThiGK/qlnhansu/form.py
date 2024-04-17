from django import forms
from .models import NHANSU, DONVI, NHANSUDONVI



class NhanSuForm(forms.ModelForm):
 class Meta:
    model = NHANSU
    fields = "__all__"


class Form(forms.Form):
    hoten = forms.CharField(required=False)
    donvi = forms.ChoiceField(required=False, choices=())
