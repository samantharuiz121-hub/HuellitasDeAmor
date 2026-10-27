# Actualiza los campos para usar texto sencillo sin listas de opciones.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mascotas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mascota",
            name="especie",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="mascota",
            name="estado",
            field=models.CharField(default="Disponible", max_length=20),
        ),
        migrations.AlterField(
            model_name="solicitudadopcion",
            name="estado",
            field=models.CharField(default="Pendiente", max_length=20),
        ),
        migrations.AlterField(
            model_name="solicitudadopcion",
            name="mascota",
            field=models.ForeignKey(on_delete=models.PROTECT, to="mascotas.mascota"),
        ),
        migrations.AlterField(
            model_name="solicitudadopcion",
            name="adoptante",
            field=models.ForeignKey(on_delete=models.PROTECT, to="mascotas.adoptante"),
        ),
        migrations.AlterField(
            model_name="adopcion",
            name="solicitud",
            field=models.OneToOneField(on_delete=models.PROTECT, to="mascotas.solicitudadopcion"),
        ),
        migrations.AlterField(
            model_name="mascota",
            name="voluntario",
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, to="mascotas.voluntario"),
        ),
    ]
