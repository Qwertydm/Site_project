from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Добро пожаловать!',
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def news(request):
    return render(request, 'main/contacts.html')
