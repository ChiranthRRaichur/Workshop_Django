from django import forms
from app3.models import Customers

class input1_form(forms.ModelForm):
    class Meta:
        model = Customers
        fields=['firstname','lastname','adhaar_num','cust_id']




# class inputform(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields=['name','aadhar','pincode']