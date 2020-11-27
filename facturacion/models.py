from django.db import models
from django.utils import timezone

# Create your models here.

class productos (models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150,default='producto')
    cantidad = models.BigIntegerField(default=0)
    costo = models.DecimalField(max_digits=8,decimal_places=2)
    margen = models.DecimalField(max_digits=8,decimal_places=4)
    ubicacion = models.CharField(max_length=8)
    empresa = models.ForeignKey('empresas',on_delete=models.CASCADE)

    def __str__(self):
        return 'Nombre: '+self.nombre+'   -   Precio: '+str(self.costo*self.margen)

class empresas (models.Model):
    nombre = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=20)
    cuit = models.CharField(max_length=13)
    cond_afif = models.CharField(max_length=8)
    tipo = models.CharField(max_length=4)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    pais = models.CharField(max_length=10)
    codpost = models.CharField(max_length=8)
    bonificacion = models.DecimalField(max_digits=8,decimal_places=4)

    def __str__(self):
        return self.nombre+' - '+self.tipo

class personas(models.Model):
    apellido = models.CharField(max_length=15)
    nombre = models.CharField(max_length=15)
    cargo = models.CharField(max_length=15)
    mail = models.EmailField()
    nacimiento = models.DateField(blank=True,null=True)
    empleado = models.BooleanField()
    esposa = models.BooleanField()
    hijos = models.IntegerField()
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    pais = models.CharField(max_length=10)
    codpost = models.CharField(max_length=8)
    empresa = models.ForeignKey('empresas',on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido+', '+self.nombre+'  -  '+str(self.empresa)

class telefonos (models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=8)
    persona = models.ForeignKey('personas',on_delete=models.CASCADE)

class facturas(models.Model):
    cliente = models.ForeignKey('empresas',on_delete=models.CASCADE)
    vendedor = models.ForeignKey('personas',on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)

class items_factura(models.Model):
    factura = models.ForeignKey('facturas',on_delete=models.CASCADE)
    producto = models.ForeignKey('productos',on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6,decimal_places=2)