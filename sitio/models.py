from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    """Model definition for Alumno."""

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    carnet = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Alumno."""

        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        """Unicode representation of Alumno."""
        return self.nombre

class Materia(models.Model):
    """Model definition for Materia."""

    nombre = models.CharField(max_length=50)
    creditos = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Materia."""

        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        """Unicode representation of Materia."""
        return self.nombre

class Pensum(models.Model):
    """Model definition for Pensum."""

    grado = models.CharField(max_length=50)
    seccion = models.CharField(max_length=1)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materias = models.ManyToManyField(Materia, through='DetallePensum')

    class Meta:
        """Meta definition for Pensum."""

        verbose_name = 'Pensum'
        verbose_name_plural = 'Pensums'

    def __str__(self):
        """Unicode representation of Pensum."""
        return self.pk

class DetallePensum (models.Model):
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.CharField(max_length=5)

class DetallePensumInLine(admin.TabularInline):
    model = DetallePensum
    extra = 1


class PensumAdmin(admin.ModelAdmin):
    inlines = (DetallePensumInLine,)


class MateriaAdmin (admin.ModelAdmin):
    inlines = (DetallePensumInLine,)

