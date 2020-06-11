from django.db import models
import uuid


class Cliente(models.Model):
	identidad = models.CharField(max_length = 15, primary_key = True)
	p_nombre = models.CharField(max_length = 20)
	s_nombre = models.CharField(max_length = 20)
	p_apellido = models.CharField(max_length = 20)
	s_apellido = models.CharField(max_length = 20)
	fecha_nacimiento = models.DateField()
	fecha_registro = models.DateField(auto_now_add=True)

	@property
	def nombre_completo(self):
		return "{0} {1} {2} {3}".format(
									self.p_nombre,
									self.s_nombre,
									self.p_apellido,
									self.s_apellido

								).title()

	def __str__(self):
		return self.nombre_completo



class Habitacion(models.Model):
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion



class HabitacionesOcupadas(models.Model):
	registro = models.UUIDField(default=uuid.uuid4, primary_key=True)
	Habitacion = models.ForeignKey(Habitacion, on_delete = models.CASCADE)
	no_habitacion = models.CharField(max_length=5)
	fecha_registro = models.DateField()
	fecha_retiro = models.DateField()



	@property
	def registro_detallado(self):
		return "{0} {1} {2} ".format(
									self.Habitacion,
									self.no_habitacion,
									self.fecha_retiro
								)

	@property
	def dias_ocupados(self):
		return (self.fecha_retiro-self.fecha_registro).days



class EncabezadoFactura(models.Model):
	factura = models.UUIDField(default=uuid.uuid4, primary_key=True)
	Cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
	Fecha_proceso = models.DateField(auto_now_add=True)
	Fecha_modifica = models.DateField(auto_now_add=True)

class DetalleFactura(models.Model):
	factura = models.ForeignKey(EncabezadoFactura, on_delete = models.CASCADE)
	habitacion = models.ForeignKey(HabitacionesOcupadas, on_delete = models.CASCADE)
	precio = models.IntegerField()

	@property
	def monto(self):
		return self.precio * self.habitacion.dias_ocupados
		
