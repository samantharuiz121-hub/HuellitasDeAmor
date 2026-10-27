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
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10)
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, default="Disponible")
    fecha_rescate = models.DateField()
    voluntario = models.ForeignKey(Voluntario, on_delete=models.SET_NULL, null=True, blank=True)

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
    mascota = models.ForeignKey(Mascota, on_delete=models.PROTECT)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.PROTECT)
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="Pendiente")

    def __str__(self):
        return str(self.id)


class Adopcion(models.Model):
    solicitud = models.OneToOneField(SolicitudAdopcion, on_delete=models.PROTECT)
    fecha_adopcion = models.DateField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
