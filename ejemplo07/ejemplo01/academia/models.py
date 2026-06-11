import datetime
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.cedula} - Edad: {self.edad} - Año de nacimiento: {self.obtener_anio_nacimiento()} - Ciudad: {self.obtener_ciudad()}"

    def obtener_anio_nacimiento(self):
        anio_actual = datetime.datetime.now().year
        return anio_actual - self.edad

    def obtener_ciudad(self):
        if self.cedula.startswith("11"):
            return "Loja"
        return "Otra ciudad"