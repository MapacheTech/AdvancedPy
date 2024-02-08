from lib import *



"""obj_poly_1 = Poligono(10,18)
print(obj_poly_1)
print(f"Num lados: {obj_poly_1.numLado }")
print(obj_poly_1.nomPoly())
print(obj_poly_1.periPoly())

obj_poly_2 = PoligonoRegular(5,20,3)
print(obj_poly_2)
print(obj_poly_2.nomPoly())
print(f"El perimetro del poligono es: {obj_poly_2.periPoly()}")
print(f"El area del perimetro es: {obj_poly_2.areaPoly()}")
print(f"El area es mayor a 200? : {obj_poly_2.chkArea()}")
obj_poly_2.setColor("Rosa ulcera")
print(f"El color es: {obj_poly_2.color}")

num1 = 10
num2 = 0
num3 = "10"


try:
    div = num1 / num2
except ZeroDivisionError:
    print("No puedes dividir entre 0...")

try:
    div2 = num1 / num3
except TypeError:
    print("No puedes dividir Strings entre numeros")
    
except Exception as e:
    print(f"Error desconocido: {e} ")

print("Hello2")"""


art1=art(10256,"Coca-Cola","Canada Dry 500ml")

art1.setDescuento(10)
art1.setPeso(10)
art1.setInventario(10)
art1.setPrecio(25.00)
print(art1)

cart1 = cart("ABC123")
#print(cart1)

cart2 = cart("DEF456")
#print(cart2)

cart3 = cart("GHI789")
#print(cart3)

art2 = art(10165,"Sabritas","Rancheritos 500gr")
art2.setDescuento(25)
art2.setPeso(500)
art2.setInventario(5)
art2.setPrecio(22.00)
#print(art2)

art3 = art(11608,"Bimbo","Mantacadas 150gr")
art3.setPeso(150)
#art3.setInventario(5)
art3.setPrecio(22.00)
#print(art3)
art3.setInventario(20)
art3.setDescuento(0)

cart1.addArticulo(art1)
cart1.addArticulo(art1)
cart1.addArticulo(art1)
cart1.addArticulo(art2)
cart1.addArticulo(art3)
print(cart1)
print("---------------------------------")
print(cart1.objArticulos[0])
print(cart1.objArticulos[0].nombre)#en aso de solo querer un dato en específico se agrega "." y lo que quieres q imprima
print(cart1.objArticulos[1].nombre)
print(art1.inventario)
print(art2.inventario)
print(art3.inventario)
print("--------------------------------------")
print(f"Carrito: {cart1.idCart}")

print(f"Total: ${cart1.getTotal()} mxn")

printTicket(cart1)