from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    context = {}
    context['birthday'] = '1 May 1986'
    context['website'] = 'www.example.com'
    context['phone'] = '0918-8384-918'
    context['city'] = 'Kermanshah, IRAN'
    context['age'] = '37'
    context['degree'] = 'MSC'
    context['freelance'] = 'Available'
    context['email'] = 'golshnai.ma@gmail.com'

    return render(request, 'website/about.html',context)


def contact_view(request):
    context = {'location': 'Kermanshah, IRAN', 'email': 'Golshani.ma@gmail.com', 'call': '+98 918 83 84 918'}
    return render(request, 'website/contact.html', context)


def skills_view(request):
    return render(request, 'website/skills.html')


def education_view(request):
    return render(request, 'website/education.html')


def project_view(request):
    return render(request, 'website/projects.html')


def test_view(request):
    context = {'firstname': 'MohammadAmin', 'lastname': 'Golshani'}
    return render(request, 'website/test.html', context)
