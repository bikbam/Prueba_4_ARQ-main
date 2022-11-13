from django.db import models

# Create your models here.
class EmpresaPyme (models.Model):
    CHILE = 'CHI'
    SANTANDER = 'SAN'
    SCOTIABANK = 'SCO'
    ESTADO = 'EST'
    FALABELLA = 'FAL'
    DESARROLLO = 'DES'
    BICE = 'BIC'
    CONSORCIO = 'CON'
    BCI = 'BCI'
    ITAU = 'ITA'
    SECURITY = 'SEC'
    CITIBANK = 'CIT'
    INTERNACIONAL = 'INT'
    
    CORRIENTE = 'COR'
    AHORRO = 'AHOR'
        
    BANCO_OPCIONES = [
        (CHILE, 'Banco de Chile'),
        (SANTANDER, 'Banco Santander-Santiago'),
        (SCOTIABANK, 'Banco Scotiabank'),
        (ESTADO, 'Banco del Estado de Chile'),
        (FALABELLA, 'Banco Falabella'),
        (DESARROLLO, 'Banco del Desarrollo'),
        (BICE, 'Banco Bice'),
        (CONSORCIO, 'Banco Consorcio'),
        (BCI, 'Banco de Credito e Inversiones'),
        (ITAU, 'Banco Itau'),
        (SECURITY, 'Banco Security'),
        (CITIBANK, 'Citibank N.A'),
        (INTERNACIONAL, 'Banco Internacional'),
    ]
    
    CUENTA_OPCIONES = [
        (CORRIENTE, 'Cuenta Corriente/Cuenta Vista'),
        (AHORRO, 'Cuenta Ahorro'),
    ]

    idPyme = models.AutoField(primary_key= True, verbose_name= 'ID Pyme')
    nombrePyme = models.CharField(max_length=50, verbose_name='Nombre Pyme')
    rutPyme = models.CharField(max_length= 12, verbose_name= 'Rut Pyme')
    bancoPyme = models.CharField(max_length= 4, choices = BANCO_OPCIONES, verbose_name= 'Banco Pyme')
    tipoCuentaPyme = models.CharField(max_length= 4, choices = CUENTA_OPCIONES, verbose_name= 'Tipo cuenta Banco Pyme')
    cuentaBancoPyme = models.CharField(max_length= 15, verbose_name= 'Cuenta Bancaria Pyme')
    correoPyme = models.EmailField(max_length=100, verbose_name='Email Pyme')

    def _str_(self) -> str:
        return self.nombrePyme


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def _str_(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='ID Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre Producto')
    descripcionProducto = models.TextField(max_length=500, verbose_name='Descripcion Producto')
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activoProducto = models.BooleanField(default=True, verbose_name='active')
    precioProducto = models.PositiveIntegerField(verbose_name= 'Precio Producto')
    imagenProducto = models.ImageField(upload_to='imgprodcuto')
    stockProducto = models.PositiveIntegerField(verbose_name= 'Stock Producto')
    pymeProducto = models.ForeignKey(EmpresaPyme, on_delete=models.CASCADE)
    
    def _str_(self) -> str:
        return self.nombreProducto
    
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, verbose_name='ID Cliente')
    rutCliente = models.IntegerField(max_length= 12, verbose_name= 'Rut Cliente')
    dvRut = models.IntegerField(max_length= 1, verbose_name= 'DV Rut')
    nombreCliente= models.CharField(max_length=50, verbose_name='Nombre Cliente')
    apellidoCliente= models.CharField(max_length=50, verbose_name='Apellido Cliente')
    correoCliente= models.EmailField(max_length=50, verbose_name='Correo Cliente')
    direccionCliente= models.CharField(max_length=50, verbose_name='Direccion Cliente')
    telefonoCliente= models.CharField(max_length=9, verbose_name='Telefono Cliente')

    def _str_(self) -> str:
        return self.nombreCliente
    
class registro(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='ID Usuario')
    nombreUsuario= models.CharField(max_length=50, verbose_name='Nombre Usuario')
    correoUsuario= models.EmailField(max_length=50, verbose_name='Correo Usuario')
    contraseñaUsuario= models.CharField(max_length=50, verbose_name='Contraseña Usuario')
    telefonoUsuario= models.CharField(max_length=9, verbose_name='Telefono')

    def _str_(self) -> str:
        return self.idUsuario

class venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name='ID Venta')
    idProducto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idPyme = models.ForeignKey(EmpresaPyme, on_delete=models.CASCADE)
    cantidadProducto= models.PositiveIntegerField(verbose_name='Cantidad de producto')
    totalVenta = models.PositiveIntegerField(verbose_name='Total venta')

    def _str_(self) -> str:
        return self.idVenta

class delivery(models.Model):
    idDelivery = models.AutoField(primary_key=True, verbose_name='ID delivery')
    comentarioDelivery= models.CharField(max_length=50, verbose_name='Comentario delivery')
    idventa=models.ForeignKey(venta,on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.idDelivery


class boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True, verbose_name='ID Boleta')
    idVenta=models.ForeignKey(venta,on_delete=models.CASCADE)
    fechaBoleta= models.DateTimeField(verbose_name='Fecha de Boleta')

    def _str_(self) -> str:
        return self.idBoleta

class pagoPyme(models.Model):
    idPago = models.AutoField(primary_key=True, verbose_name='ID Pago')
    idPyme =models.ForeignKey(EmpresaPyme, on_delete=models.CASCADE)
    montoTotal= models.IntegerField(verbose_name='monto Pago')
    fechaPago=models.DateField(verbose_name='fecha Pago')
    def _str_(self) -> str:
        return self.idPago

class comentarioProducto (models.Model):
    idComentario= models.AutoField(primary_key=True, verbose_name='ID Comentario')
    idVenta=models.ForeignKey(venta,on_delete=models.CASCADE)
    idCliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    comentarioProducto=models.CharField(max_length=500, verbose_name='Comentario Produto')
    valoracion=models.PositiveIntegerField(verbose_name='Valoracion')

    def _str_(self) -> str:
        return self.idComentario
    
