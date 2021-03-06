from  django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Propertytype,Property,Phone
# class 

class PhoneForm(forms.ModelForm):
    class Meta:
    
        model = Phone
        fields = '__all__'

class AddlandForm(forms.ModelForm):
    description = forms.Textarea(attrs={'cols':2,'rows':2,'placeholder':'enter description about the property'})
    image = forms.ImageField(required=True)
    class Meta:

        model = Property
        fields = ['property_type','price','location','description',
        'sqrt','sale_type','name','image','image1','image2','image3',
        'image4','image5']

class AddhouseForm(forms.ModelForm):
    description = forms.Textarea(attrs={'cols':2,'rows':2,'placeholder':'enter description about the property'})
    class Meta:

        model = Property
        fields = ['property_type','price','location','name','description',
        'sqrt','sale_type','image','image1','image2','image3',
        'image4','image5','bed','bath',]

