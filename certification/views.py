from django.shortcuts import render
from .models import Languages
from .forms import AddCertification


def index(request):
    name = "Junior Steve"
    age = 47
    languages = Languages.objects.all()
    add_certification_form = AddCertification()
    context = {
        "age": age,
        "name": name,
        "languages": languages,
        "form": add_certification_form,
    }
    return render(request, "index.html", context)
