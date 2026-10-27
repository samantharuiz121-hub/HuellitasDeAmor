
from django.contrib import admin
from .models import Voluntario, Mascota, Adoptante, SolicitudAdopcion, Adopcion

admin.site.register(Voluntario)
admin.site.register(Mascota)
admin.site.register(Adoptante)
admin.site.register(SolicitudAdopcion)
admin.site.register(Adopcion)
