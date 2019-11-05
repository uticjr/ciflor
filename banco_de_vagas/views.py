from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .models import Vaga
from assets.Canditato import CanditatoForm


# Create your views here.
def home(request):
    data = {}
    data['vagas'] = Vaga.objects.all()
    data['canditato'] = {'nome': '', 'email': '', 'curriculo': ''}
    return render(request, 'site/base.html', data)


class CanditatoModal(BSModalCreateView):
    template_name = 'site/modal-teste.html'
    form_class = CanditatoForm
    success_message = 'Sucesso: Currículo enviado'
    success_url = reverse_lazy('home')


def enviar(request):
    send_mail(subject='Vaga Estágio', message='Olá',from_email='romomulo.sa153@live.com',recipient_list=['romulo.gabss@gmail.com'], fail_silently=False)
    return HttpResponse("""
        <h1>Enviou</h1>
    """)
