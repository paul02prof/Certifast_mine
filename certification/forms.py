from django import forms
from .models import Certifications, Category, Institutions, Prerequisites, Languages

class AddCertificationForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'description': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'level_of_difficulty': forms.Select(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'category': forms.Select(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'price': forms.NumberInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'duration_of_validity': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'institution': forms.Select(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'exam_site': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'prerequisites': forms.Select(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'link': forms.URLInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'discounts': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'languages': forms.Select(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Category Name'}),
        }

class InstitutionsForm(forms.ModelForm):
    class Meta:
        model = Institutions
        fields = ['name', 'accepted_zones', 'about']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Institution Name'}),
            'accepted_zones': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Accepted Zones'}),
            'about': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'About'}),
        }

class PrerequisitesForm(forms.ModelForm):
    class Meta:
        model = Prerequisites
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Description'}),
        }

class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['code', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Language Code (e.g. EN)'}),
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Language Name'}),
        }

