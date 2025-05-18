from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, FormView

from .forms import AddCertificationForm, CategoryForm, InstitutionsForm, PrerequisitesForm, LanguagesForm
from .models import Languages, Category, Institutions, Prerequisites


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
            model_class = Category
        elif model_name == 'institution':
            form = InstitutionsForm(request.POST)
            model_class = Institutions
        elif model_name == 'prerequisites':
            form = PrerequisitesForm(request.POST)
            model_class = Prerequisites
        elif model_name == 'languages':
            form = LanguagesForm(request.POST)
            model_class = Languages
        else:
            return JsonResponse({'error': 'Invalid model type'}, status=400)

        if form.is_valid():
            new_item = form.save()
            items = model_class.objects.all()
            options = [{'value': item.id, 'label': str(item)} for item in items]

            return JsonResponse({
                'success': True,
                'new_id': new_item.id,
                'options': options
            })
        else:
            return JsonResponse({'error': form.errors}, status=400)
