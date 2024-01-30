class art:
    def __init__(self, idArt, marca, nombre, precio=None, peso=None, descuento=None, inventario=None):
        self.id = idArt
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.descuento = descuento        
        self.inventario = inventario
        pass
    
    def __str__(self):
        return f"idArt: {self.id}, Marca: {self.marca}, nombre: {self.nombre}, precio: {self.precio}, peso: {self.peso}, descuento: {self.descuento}, inventario: {self.inventario}"
    
    def setPrecio(self, precio):
        self.precio = precio
        return 0
        
class cart(art):
     def __init__(self, marca, nombre, precio, peso, descuento, id, piezas, costoTotal, iva, ahorroTotal):
         super().__init__(marca, nombre, precio, peso, descuento, id, piezas)
         self.costoTotal = costoTotal
         self.iva = iva
         self.ahorroTotal = ahorroTotal
         
         
         pass
     
     
