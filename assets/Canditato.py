from django.db import models
from banco_de_vagas.models import Canditato
from bootstrap_modal_forms.forms import BSModalForm


class CanditatoForm(BSModalForm):
    class Meta:
        model = Canditato
        fields = '__all__'
