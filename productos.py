class Productos:
	def __init__(self, codigo, name, precio, cat):
		self.codigo = codigo
		self.name = name
		self.precio = precio
		self.cat = cat
	def presentar(self):
		print('Abarroteria la mejor, ahorra y compra al por mayor', self.name)
		
a1 = Productos(1, 'Aceite', 12.5, 'Cocina')
a2 =Productos(2, 'Jabon', 3.80, 'Limpieza')
a1.presentar()
print('Codigo:', a1.codigo, 'Producto:', a1.name, 'Precio:', 'Q', a1.precio, 'Categoría:', a1.cat)
print('Codigo:', a2.codigo, 'Producto:', a2.name, 'Precio:', 'Q', a2.precio, 'Categoría:', a2.cat)

class Calcular:
	suma = a1.precio + a2.precio
	print('Total a cancelar:', suma)


	
	



	
