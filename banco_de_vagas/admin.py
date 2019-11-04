from django.contrib import admin
from .models import (
    Empresa,
    Vaga,
)

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Vaga)
