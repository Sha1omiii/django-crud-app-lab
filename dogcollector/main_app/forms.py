from django import forms
from .models import Dog, Owner, Toy

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'description', 'age', 'owner']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name']  # Ensure this list matches actual model fields

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ['name', 'dogs']
