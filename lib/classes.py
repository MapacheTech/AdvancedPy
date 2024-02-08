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
    
    def setPeso(self,peso):
        self.peso = peso
        return 0
    
    def setDescuento(self,descuento):
        self.descuento = descuento
        return 0
    
    def setInventario(self,inventario):
        self.inventario = inventario
        return 0
    
    def getPrecioDcto(self):
        if self.descuento != None:
            precioDescuento = self.precio - (self.precio * (self.descuento/100))
        else:
            precioDescuento = self.precio
        return precioDescuento
    
    def getDcto(self):
        if self.descuento != None:
            precioDcto = ( self.precio * (self.descuento/100))
        else:
            precioDcto = 0
        return precioDcto
    
class cart():
    def __init__(self, idCart):
         self.idCart = idCart
         self.objArticulos = []        
         pass
    
    def __str__(self):
        printCart = f"Ticket #: {self.idCart} \n"
        if len(self.objArticulos) >= 1:
            for i in range(0, len(self.objArticulos),1):
                printCart += f"{self.objArticulos[i].id} {self.objArticulos[i].nombre} $ {self.objArticulos[i].precio} mxn\n -${self.objArticulos[i].getDcto()}mxn\n"
        else:
            printCart += f"Carrito vacio"
        return printCart
    
    def addArticulo(self, objArt):
        if type (objArt.inventario) != type(None):
            if objArt.inventario >= 1:
                objArt.inventario -= 1
                self.objArticulos.append(objArt)
            else:
                print(f"No hay inventario de: ({objArt.nombre})")
        else:
            print("Inventario no definido")
        return 0
    def getTotal(self):
        total = 0
        for i in range(0, len(self.objArticulos),1):
            total += self.objArticulos[i].getPrecioDcto()
        return total 
    
    def getTotalDcto(self):
        total = 0
        for i in range(0, len(self.objArticulos),1):
            total += self.objArticulos[i].getDcto()
        return total 
        pass
     
     
