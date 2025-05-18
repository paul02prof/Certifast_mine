from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, FormView

from .forms import AddCertificationForm, CategoryForm, InstitutionsForm, PrerequisitesForm, LanguagesForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddCertificationForm()
        return context


class AddCertificationView(FormView):
    template_name = 'add_certification.html'
    form_class = AddCertificationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_form'] = CategoryForm()
        context['institutions_form'] = InstitutionsForm()
        context['prerequisites_form'] = PrerequisitesForm()
        context['languages_form'] = LanguagesForm()
        context['csrf_token'] = get_token(self.request)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AddRelatedView(View):
    """Handle AJAX requests for adding related models."""

    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, model_name, *args, **kwargs):
        if model_name == 'category':
            form = CategoryForm(request.POST)
        elif model_name == 'institution':
            form = InstitutionsForm(request.POST)
        elif model_name == 'prerequisites':
            form = PrerequisitesForm(request.POST)
        elif model_name == 'languages':
            form = LanguagesForm(request.POST)
        else:
            return JsonResponse({'error': 'Invalid model type'}, status=400)

        if form.is_valid():
            form.save()
            return redirect(reverse('add_certification'))
        else:
            return JsonResponse({'error': form.errors}, status=400)
