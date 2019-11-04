from django.shortcuts import render
from .models import Vaga


# Create your views here.
def home(request):
    data = {}
    data['vagas'] = Vaga.objects.all()
    return render(request, 'site/base.html', data)
