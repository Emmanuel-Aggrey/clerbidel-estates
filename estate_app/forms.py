from  django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Propertytype,Property
# class 

class AddlandForm(forms.ModelForm):
    description = forms.Textarea(attrs={'cols':1,'rows':2,'placeholder':'enter description about the property'})
    image = forms.ImageField(required=True)
    class Meta:

        model = Property
        fields = ['property_type','price','location','description',
        'sqrt','sale_type','image','image1','image2','image3',
        'image4','image5']

class AddhouseForm(forms.ModelForm):
    description = forms.Textarea(attrs={'cols':1,'rows':2,'placeholder':'enter description about the property'})
    class Meta:

        model = Property
        fields = ['property_type','price','location','name','description',
        'sqrt','sale_type','image','image1','image2','image3',
        'image4','image5','bed','bath',]

