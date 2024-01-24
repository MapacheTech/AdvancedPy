from lib import *



obj_poly_1 = Poligono(10,18)
print(obj_poly_1)
"""print(f"Num lados: {obj_poly_1.numLado }")"""
print(obj_poly_1.nomPoly())
print(obj_poly_1.periPoly())

obj_poly_2 = PoligonoRegular(5,20,2)
print(obj_poly_2)
print(obj_poly_2.nomPoly())
print(obj_poly_2.periPoly())