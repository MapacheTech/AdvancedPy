from lib import *



obj_poly_1 = Poligono(10,18)
print(obj_poly_1)
"""print(f"Num lados: {obj_poly_1.numLado }")"""
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

print("Hello2")
