from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Certifications, Category, Institutions, Prerequisites, Languages

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddCertificationForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'js-tags block w-full mt-1 p-2 border border-gray-300 rounded'})
    )

    prerequisites = forms.ModelMultipleChoiceField(
        queryset=Prerequisites.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'js-tags block w-full mt-1 p-2 border border-gray-300 rounded'})
    )

    languages = forms.ModelMultipleChoiceField(
        queryset=Languages.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'js-tags block w-full mt-1 p-2 border border-gray-300 rounded'})
    )

    class Meta:
        model = Certifications
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'description': forms.Textarea(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'level_of_difficulty': forms.Select(attrs={
                'class': 'block w-full mt-1 p-2 pr-8 border border-gray-300 rounded appearance-none bg-white bg-no-repeat bg-[length:16px] bg-[center_right_12px] bg-[url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'none\' viewBox=\'0 0 24 24\' stroke=\'%236b7280\'%3E%3Cpath stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M19 9l-7 7-7-7\'%3E%3C/path%3E%3C/svg%3E")]'}),
            'price': forms.NumberInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'duration_of_validity': forms.TextInput(
                attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'institution': forms.Select(
                attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'exam_site': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'link': forms.URLInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
            'discounts': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded'}),
        }

    def save(self, commit=True):
        """Override save to handle many-to-many relationships."""
        cleaned_data = self.cleaned_data

        category_items = cleaned_data.pop('category', None)
        prerequisites_items = cleaned_data.pop('prerequisites', None)
        languages_items = cleaned_data.pop('languages', None)

        instance = super().save(commit=False)

        if commit:
            instance.save()

            if category_items:
                instance.category.set(category_items)

            if prerequisites_items:
                instance.prerequisites.set(prerequisites_items)

            if languages_items:
                instance.languages.set(languages_items)

            self.save_m2m()

        return instance


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'block w-full mt-1 p-2 border border-gray-300 rounded',
                    'placeholder': 'Category Name',
                }
            ),
        }


class InstitutionsForm(forms.ModelForm):
    class Meta:
        model = Institutions
        fields = ['name', 'accepted_zones', 'about']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'block w-full mt-1 p-2 border border-gray-300 rounded',
                    'placeholder': 'Institution Name'
                }
            ),
            'accepted_zones': forms.TextInput(
                attrs={
                    'class': 'block w-full mt-1 p-2 border border-gray-300 rounded',
                    'placeholder': 'Accepted Zones'
                }
            ),
            'about': forms.Textarea(
                attrs={
                    'class': 'block w-full mt-1 p-2 border border-gray-300 rounded',
                    'placeholder': 'About',
                }
            ),
        }


class PrerequisitesForm(forms.ModelForm):
    class Meta:
        model = Prerequisites
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Title'}),
            'description': forms.Textarea(
                attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded', 'placeholder': 'Description'}),
        }


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['code', 'name']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded',
                                           'placeholder': 'Language Code (e.g. EN)'}),
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 p-2 border border-gray-300 rounded',
                                           'placeholder': 'Language Name'}),
        }
