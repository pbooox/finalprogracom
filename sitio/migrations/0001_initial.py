# Generated by Django 2.2.7 on 2019-11-18 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('carnet', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='DetallePensum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=50)),
                ('seccion', models.CharField(max_length=1)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Alumno')),
                ('materias', models.ManyToManyField(through='sitio.DetallePensum', to='sitio.Materia')),
            ],
            options={
                'verbose_name': 'Pensum',
                'verbose_name_plural': 'Pensums',
            },
        ),
        migrations.AddField(
            model_name='detallepensum',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Materia'),
        ),
        migrations.AddField(
            model_name='detallepensum',
            name='pensum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Pensum'),
        ),
    ]
