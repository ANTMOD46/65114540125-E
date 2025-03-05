from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import *

# Create your views here.
def AS(requrest):
    All = A.objects.all()
    return render(requrest, 'A.html', {'mod': All})

class ES(UpdateView):
    model = A
    template_name = 'E.html'
    success_url = reverse_lazy('A')


