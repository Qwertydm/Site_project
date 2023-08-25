from django.shortcuts import render
from .models import Novosti
from django.views.generic import DetailView

# Create your views here.
def nvsti_home(request):
    nvsti = Novosti.objects.order_by('-date_nv')
    return render(request, 'nvsti/nvsti_home.html', {'nvsti': nvsti})

class NewsDetailView_nv(DetailView):
    model = Novosti
    template_name = 'nvsti/details_nv_view.html'
    context_object_name = 'novost'