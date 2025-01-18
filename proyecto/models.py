from django.db import models

# Create your models here.
class Inventario(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    marca = models.CharField(max_length=30, null=False)
    modelo = models.CharField(max_length=30, null=False)
    precio = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    stock = models.IntegerField(null=False)
    CATEGORIA_INSTRUMENTO = {
        ('C', 'Cuerda'),
        ('V', 'Viento'),
        ('P','Percusión'),
        ('T', 'Tecla'),
        ('A', 'Arco'),
        ('E', 'Electrónico')
    }
    categoria = models.CharField(max_length=30, choices=CATEGORIA_INSTRUMENTO, null= False)
    picture = models.ImageField(upload_to="instrumento_image", null=True)
    
    def __str__(self)-> str:
        return f'{self.nombre} {self.marca}'
 
class Cliente(models.Model):
    cedula = models.IntegerField(unique=True, null=False)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    telefono = models.IntegerField(null=False)
    email = models.CharField(max_length=150, null=False)
    direccion = models.CharField(max_length=250, null=False)

    def __str__(self)-> str:
        return f'{self.nombre} {self.apellido}'
 
   
class Ventas(models.Model):
    fecha_venta = models.DateField()
    cliente_id = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    producto_id = models.ForeignKey(Inventario, on_delete=models.RESTRICT)
     
    def __str__(self)-> str:
        return f'{self.total}'
    
class Proveedor(models.Model):
    cedula = models.IntegerField(unique=True, null=False)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=True)
    telefono = models.IntegerField(null=False)
    email = models.CharField(max_length=150, null=False)

    def __str__(self)-> str:
        return f'{self.nombre} {self.apellido}'

class Cardex(models.Model):
    fecha_movimiento = models.DateField(null=False)
    instrumento_id = models.ForeignKey(Inventario, on_delete=models.RESTRICT)
    TIPO_MOVIMIENTO = {
        ('E', 'Entrada'),
        ('S', 'Salida'),
    }
    tipo = models.CharField(max_length=30, choices=TIPO_MOVIMIENTO, null= False)
    cantidad = models.IntegerField(null=False)
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.RESTRICT)
