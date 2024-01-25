class Poligono:
    def __init__(self,numLado, sizeLado):
        self.numLado = numLado
        self.sizeLado = sizeLado
        pass

    def __str__(self):
        return f"Número de Lados : {self.numLado} y Tamaño del lado: {self.sizeLado} "
    
    def nomPoly(self):
        match self.numLado:
            case 3:
                return "Tu poligono es un triángulo"
            case 4:
                return "Tu poligono es un cuadrado"
            case 5:
                return "Tu poligono es un pentágono"
            case 6:
                return "Tu poligono es un hexagono"
            case 7:
                return "Tu poligono es un heptagono"
            case 8:
                return "Tu poligono es un octágono"
            case 9:
                return "Tu poligono es un eneágono"
            case 10:
                return "Tu poligono es un decágono"
            case _:
                return f"Tu poligono tiene {self.numLado} lados"
            
    def periPoly(self):
        perimetro = self.numLado * self.sizeLado
        return perimetro
             

class PoligonoRegular(Poligono):
    def __init__(self, numLado, sizeLado, apotema):
        super().__init__(numLado, sizeLado,)
        self.apotema = apotema
        pass
    def __str__(self):
        return f"Número de lados: {self.numLado}, Size lado: {self.sizeLado}, Apotema: {self.apotema}"
    
    def areaPoly(self):
        area = (self.apotema * super().periPoly()) / 2
        return area
    
    def chkArea(self):
        if self.areaPoly() >= 200:
            return "Si"
        else:
            return "No"
    def setColor(self,color):
        self.color = color
        return f"El color es: {self.color}"