from django.shortcuts import render


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')


def skills_view(request):
    return render(request, 'website/skills.html')


def education_view(request):
    return render(request, 'website/education.html')


def project_view(request):
    return render(request, 'website/projects.html')
# Create your views here.
