from django.db import models

# Create your models here.

choicesTrabajo= (("P","Programador"),
                 ("A","Administrador"),
                 ("C","Chef"),
                 ("N","Ninguno"))

class Personal(models.Model):
     nombre= models.CharField("Nombre",max_length=100 , null=False ,blank=False, unique=True)
     apellido= models.CharField("Apellido", max_length=120 , null=False, blank=False , unique=True)
     edad= models.IntegerField("Edad",null=False , blank=False)

     class Meta:
         verbose_name= "Personal"
         verbose_name_plural= "El Personal"

     def __str__(self):
         return  self.nombre

class Empleo(models.Model):
    nombre= models.CharField("Nombre Empleo", max_length=90 , null=False , blank=False)
    aspiracion =models.TextField("Aspiracion " , max_length=120 , null=True, blank=False)
    experiencia= models.CharField("Experiencias",choices=choicesTrabajo , max_length=1)
    persona_empleo= models.ForeignKey(Personal, on_delete=models.CASCADE)

    class Meta:
        verbose_name= "Empleo"
        verbose_name_plural="Empleos"

    def __str__(self):
        return self.nombre
