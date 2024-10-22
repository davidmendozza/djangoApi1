from django.db import models

# Create your models here.
class Generos(models.Model):
    Generos_id=models.AutoField(primary_key=True)
    nombre_genero= models.CharField(max_length=255)
    
    class Meta:
        db_table= "Generos"


class Usuarios(models.Model):
    Usuario_id=models.AutoField(primary_key=True)
    nombre_usuario=models.CharField(max_length=255)
    fk_generos=models.ForeignKey(Generos,on_delete=models.CASCADE,default=0)
    class Meta:
        db_table ="usuarios"         