from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(HabitacionesOcupadas)
admin.site.register(EncabezadoFactura)
admin.site.register(DetalleFactura)