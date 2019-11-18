from django.contrib import admin
from sitio.models import Alumno, Materia, PensumAdmin, MateriaAdmin, Pensum

admin.site.register(Alumno)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Pensum, PensumAdmin)

# Register your models here.
