import math


class Circulo:
    """
    >>> Circulo(-5)
    Traceback (most recent call last):
    ...
    Exception: Imposible ingresar un radio menor o igual a 0

    >>> c =Circulo(5)
    >>> print("Perimetro: "+str(c.Perimetro()))
    Perimetro: 15.707963267948966

    >>> c =Circulo(5)
    >>> print("Area: "+str(c.Area()))
    Area: 78.53981633974483

    >>> c = Circulo(5)
    >>> c.SetRadio(2)
    >>> print("Area: "+str(c.Area())+" Perimetro: " + str(c.Perimetro()))
    Area: 12.566370614359172 Perimetro: 6.283185307179586

    >>> c = Circulo(5)
    >>> c.SetRadio(-5)
    Traceback (most recent call last):
    ...
    Exception: Imposible ingresar un radio menor o igual a 0


    >>> c =Circulo(5)
    >>> c2 = c.Multiplicacion(-1)
    Traceback (most recent call last):
    ...
    Exception: Imposible ingresar un numero menor o igual a 0

    >>> c =Circulo(2)
    >>> c2 = c.Multiplicacion(2)
    >>> print("Area: "+str(c2.Area())+" Perimetro: " + str(c2.Perimetro()))
    Area: 50.26548245743669 Perimetro: 12.566370614359172
    """
    def __init__(self, radio):
        if radio <= 0:
            raise Exception("Imposible ingresar un radio menor o igual a 0")
        else:
            self.radio = radio
    def SetRadio(self, radio):
        if radio <= 0:
            raise Exception("Imposible ingresar un radio menor o igual a 0")
        else:
            self.radio = radio
    def Perimetro(self):
        return  math.pi * self.radio 
    def Area(self):
        return  self.radio * self.radio * math.pi
    def Multiplicacion(self , n):
        if n <= 0:
            raise Exception("Imposible ingresar un numero menor o igual a 0")
        else:
            clase = Circulo(self.radio*n)
            return clase


"""
 try:
    c = Circulo(int(input('ingrese el radio ')))
    print()
    print("Perimetro: "+str(c.Perimetro()))
    print("Area: "+str(c.Area()))
    print()
    c2 = c.Multiplicacion(int(input('Circulo multiplicado por: ')))
    print()
    print("Perimetro: "+str(c2.Perimetro()))
    print("Area: "+str(c2.Area()))
except ValueError:
    print('No se pueden ingresar letras')
except Exception as e:
    print(e)
 """

import doctest
doctest.testmod()


