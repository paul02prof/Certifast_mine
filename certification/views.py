from django.shortcuts import render, redirect
from .models import Languages
from .forms import AddCertificationForm, CategoryForm, InstitutionsForm, PrerequisitesForm, LanguagesForm


def index(request):
    name = "Junior Steve"
    age = 47
    languages = Languages.objects.all()
    add_certification_form = AddCertificationForm()
    context = {
        "age": age,
        "name": name,
        "languages": languages,
        "form": add_certification_form,
    }
    return render(request, "index.html", context)

def add_certification(request):
    if request.method == 'POST':
        form = AddCertificationForm(request.POST, request.FILES)
    else:
        form = AddCertificationForm()
    context = {
        'form': form,
        'category_form': CategoryForm(),
        'institutions_form': InstitutionsForm(),
        'prerequisites_form': PrerequisitesForm(),
        'languages_form': LanguagesForm(),
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'add_certification.html', context)
