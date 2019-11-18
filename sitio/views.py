from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pensum, DetallePensum
from .forms import PensumForm

def home(request):
    return render(request,'colegio/home.html')

def pensumNuevo(request):
    if request.method == "POST":
        formulario = PensumForm(request.POST)
        if formulario.is_valid():
            pensum = Pensum.objects.create(grado=formulario.cleaned_data['grado'], seccion = formulario.cleaned_data['seccion'], alumno=formulario.cleaned_data['alumno'])
            for materia_id in request.POST.getlist('materias'):
                detallepensum = DetallePensum(materia_id=materia_id, Pensum_id = pensum.id)
                detallepensum.save()
            messages.add_message(request, messages.SUCCESS, 'Pensum Guardada Exitosamente')
    else:
        formulario = PensumForm()
    return render(request, 'colegio/pensumnuevo.html', {'formulario': formulario})  

# Create your views here.
