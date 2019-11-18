from django import forms

from .models import Pensum, Materia

class PensumForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pensum
        fields = ('grado', 'seccion', 'alumno', 'materias')

    def __init__ (self, *args, **kwargs):
        super(PensumForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Seleccione las materias"
        self.fields["materias"].queryset = Materia.objects.all()    