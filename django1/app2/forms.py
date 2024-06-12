from django import forms
from app2.models import students
class input_form(forms.ModelForm):
    class Meta:
        model=students
        fields=['name1','college1','course1']

