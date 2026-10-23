
from django.db import models


class Voluntario(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    ESPECIES = [
        ("Perro", "Perro"),
        ("Gato", "Gato"),
    ]

    ESTADOS = [
        ("Disponible", "Disponible"),
        ("En proceso", "En proceso de adopcion"),
        ("Adoptada", "Adoptada"),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Disponible"
    )
    fecha_rescate = models.DateField()
    voluntario = models.ForeignKey(
        Voluntario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mascotas"
    )

    def __str__(self):
        return self.nombre


class Adoptante(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class SolicitudAdopcion(models.Model):
    ESTADOS = [
        ("Pendiente", "Pendiente"),
        ("Aprobada", "Aprobada"),
        ("Rechazada", "Rechazada"),
    ]

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.PROTECT,
        related_name="solicitudes"
    )
    adoptante = models.ForeignKey(
        Adoptante,
        on_delete=models.PROTECT,
        related_name="solicitudes"
    )
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="Pendiente"
    )

    def __str__(self):
        return f"Solicitud {self.id} - {self.mascota.nombre}"


class Adopcion(models.Model):
    solicitud = models.OneToOneField(
        SolicitudAdopcion,
        on_delete=models.PROTECT,
        related_name="adopcion"
    )
    fecha_adopcion = models.DateField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Adopcion {self.id}"
