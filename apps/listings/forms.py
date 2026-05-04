from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'title',
            'description',
            'price',
            'category',
            'condition',
            'location_type',
            'hostel_name',
            'image',
            'status',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write a clear description of your item'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'condition': forms.Select(attrs={
                'class': 'form-select'
            }),
            'location_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'hostel_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hostel name if applicable'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }