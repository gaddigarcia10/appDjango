from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=50, unique=True)
    code = models.CharField(verbose_name="Código postal", max_length=6, unique=True)
    date = models.CharField(verbose_name="Fecha Nacimiento", max_length=20, unique=True)
    dni = models.CharField(verbose_name="DNI", max_length=10, unique=True)
    address = models.CharField(verbose_name="Direccion", max_length=80, unique=True)
    lastname = models.CharField(verbose_name="Apellido", max_length=80, unique=True)
    telephone = models.CharField(verbose_name="Número de Teléfono", max_length=20, unique=True)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}".format(self.name, self.code, self.date, self.dni, self.address,
                                                    self.lastname, self.telephone)

class Student(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=50, unique=True)
    lastname = models.CharField(verbose_name="Apellido", max_length=80, unique=True)
    code = models.CharField(verbose_name="Código postal", max_length=6, unique=True)
    date = models.CharField(verbose_name="Fecha Nacimiento", max_length=20, unique=True)
    dni = models.CharField(verbose_name="DNI", max_length=10, unique=True)
    address = models.CharField(verbose_name="Direccion", max_length=80, unique=True)
    telephone = models.CharField(verbose_name="Número de Teléfono", max_length=20, unique=True)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}".format(self.name,  self.lastname, self.code, self.date, self.dni, self.address, self.telephone)

class Classroom(models.Model):
    idn = models.CharField(verbose_name="Número Aula", max_length=50, unique=True)
    capacity = models.CharField(verbose_name="Capacidad", max_length=3, unique=True)
    floor = models.CharField(verbose_name="Edificio", max_length=20, unique=True)

    def __str__(self):
         return "{0} {1} {2} ".format(self.idn, self.capacity, self.floor)


class Matter(models.Model):
    idn = models.CharField(verbose_name="ID Materia", max_length=50, unique=True)
    name = models.CharField(verbose_name="Nombre Materia", max_length=50, unique=True)
    hour = models.CharField(verbose_name="Horas", max_length=20, unique=True)
    credit = models.CharField(verbose_name="Créditos", max_length=20, unique=True)


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.idn, self.name, self.hour, self.credit)


class Class(models.Model):
    Matter = models.ForeignKey(Matter, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    idn = models.CharField(verbose_name="ID Clase", max_length=50, unique=True)
    hour = models.CharField(verbose_name="Hora Clase", max_length=20, unique=True)


    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.Teacher, self.Matter, self.Classroom, self.idn, self.hour)