from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, FormView, DetailView
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .forms import (
    AddCertificationForm, CategoryForm,
    InstitutionsForm, PrerequisitesForm, LanguagesForm
)
from .models import Certifications,Category,Institutions,Languages,Topic,Course
from datetime import datetime
from django.core.paginator import Paginator
import plotly.graph_objects as go
import plotly.offline as opy
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

import json


def index(request):
    carousel_images = [
        "https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp",
        "https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp",
        "https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp",
        "https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp",
        "https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp",
        "https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp",
    ]
    return render(request, "index.html", {"carousel_images": carousel_images})

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        name = data.get('full_name')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'exists': True})
        else:
            username = name.lower().replace(" ", "")
            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'created': True, 'username': user.username, 'email': user.email})

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            # On récupère l'utilisateur associé à l'email

            user = User.objects.get(email=email)
            user_auth = authenticate(username=user.username, password=password)
            if user_auth is not None:
                return JsonResponse({'success': True, 'username': user.username, 'email': user.email})
            else:
                return JsonResponse({'success': False, 'error': 'Mot de passe incorrect'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Email non enregistré'})


def dashboard(request):
    # Get data from database
    certifications = Certifications.objects.all()

    # Prepare data for charts
    difficulty_counts = certifications.values_list('level_of_difficulty', flat=True)

    difficulty_counts = certifications.values_list('level_of_difficulty', flat=True)
    price_data = certifications.values_list('price', flat=True)
    institution_counts = certifications.values_list('institution__name', flat=True)

    # Chart 1: Difficulty Level Distribution
    difficulty_fig = go.Figure()
    difficulty_fig.add_trace(go.Histogram(
       x=['2', '1', '0', '2', '3', '2', '2', '1', '2', '3', '1', '1'],
       name='Difficulty Distribution',
       histnorm='percent'
    ))
    difficulty_fig.update_layout(
        title='Certification Difficulty Levels',
        xaxis_title='Difficulty Level',
        yaxis_title='Percentage',
        bargap=0.2
    )
    difficulty_div = opy.plot(difficulty_fig, auto_open=False, output_type='div')

    # Chart 2: Price Distribution
    price_fig = go.Figure()
   # price_fig.add_trace(go.Box(
   #     y=price_data,
    #    name='Price Distribution',
    #    boxpoints='all'
    #))
    price_fig.update_layout(
        title='Certification Prices',
        yaxis_title='Price ($)'
    )
    price_div = opy.plot(price_fig, auto_open=False, output_type='div')

    context = {
        'difficulty_chart': difficulty_div,
        'price_chart': price_div,
        #'institution_chart': institution_div,
        'certifications': certifications
    }

    return render(request, 'dashboard.html', context)

def certification_list(request):
    certifications = Certifications.objects.all().order_by('name')

    query = request.GET.get('q', '')


    if query:
        certifications = certifications.filter(name__icontains=query)

    # Récupérer les paramètres de filtre
    difficulty = request.GET.get('difficulty')
    category = request.GET.get('category')
    institution = request.GET.get('institution')
    language = request.GET.get('language')
    topic = request.GET.get('topic')

    # Appliquer les filtres
    if difficulty:
        certifications = certifications.filter(level_of_difficulty=difficulty)

    if category:
        certifications = certifications.filter(category__id=category)

    if institution:
        certifications = certifications.filter(institution__id=institution)

    if language:
        certifications = certifications.filter(languages__id=language)

    if topic:
        certifications = certifications.filter(topic__id=topic)

    # Pagination
    paginator = Paginator(certifications, 16)
    page_number = request.GET.get('page')
    certifications_page = paginator.get_page(page_number)

    # Préparer les données pour les filtres
    context = {
        'certifications': certifications_page,
        'difficulty_choices': dict(Certifications._meta.get_field('level_of_difficulty').choices),
        'all_categories': Category.objects.all().order_by('name'),
        'all_institutions': Institutions.objects.all().order_by('name'),
        'all_languages': Languages.objects.all().order_by('name'),
        'all_topics': Topic.objects.all().order_by('name'),
    }

    return render(request, 'certif.html', context)

def course_list(request):
    course = Course.objects.all().order_by('name')
    query = request.GET.get('q', '')

    if query:
        course = course.filter(name__icontains=query)

    # Récupérer les paramètres de filtre
    difficulty = request.GET.get('difficulty')
    category = request.GET.get('category')
    institution = request.GET.get('institution')
    language = request.GET.get('language')
    topic = request.GET.get('topic')

    # Appliquer les filtres
    if difficulty:
        course = course.filter(level_of_difficulty=difficulty)

    if category:
        course = course.filter(category__id=category)

    if institution:
        course = course.filter(institution__id=institution)

    if language:
        course = course.filter(languages__id=language)

    if topic:
        course = course.filter(topic__id=topic)

    # Pagination
    paginator = Paginator(course, 16)
    page_number = request.GET.get('page')
    course_page = paginator.get_page(page_number)

    # Préparer les données pour les filtres
    context = {
        'certifications': course_page,
        'difficulty_choices': dict(Course._meta.get_field('level_of_difficulty').choices),
        'all_categories': Category.objects.all().order_by('name'),
        'all_institutions': Institutions.objects.all().order_by('name'),
        'all_languages': Languages.objects.all().order_by('name'),
        'all_topics': Topic.objects.all().order_by('name'),
    }

    return render(request, 'course.html', context)

def path_user(request):
    institutions = Institutions.objects.all()

    return render(request, 'path.html',{'institution': institutions})


def certification_detail(request, pk):
    certification = get_object_or_404(Certifications, pk=pk)

    # Organiser les données pour le template
    context = {
        'certif': certification,
        'difficulty_levels': dict(Certifications._meta.get_field('level_of_difficulty').choices),
        'topics': certification.topic.all(),
        'categories': certification.category.all(),
        'languages': certification.languages.all(),
        'prerequisites': certification.prerequisites.all()
    }

    return render(request, 'certif_detail.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    # Organiser les données pour le template
    context = {
        'certif': course,
        'difficulty_levels': dict(Course._meta.get_field('level_of_difficulty').choices),
        'topics': course.topic.all(),
        'categories': course.category.all(),
        'languages': course.languages.all(),
        'prerequisites': course.prerequisites.all()
    }

    return render(request, 'course_detail.html', context)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certifications"] = Certifications.objects.all()
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
        """Override post to handle the form submission manually"""
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form))


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


class CertificationDetailView(DetailView):
    """Display details for a specific certification."""
    model = Certifications
    template_name = 'certification_detail.html'
    context_object_name = 'certification'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here if needed
        return context

