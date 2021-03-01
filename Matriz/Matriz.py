import numpy as np


#print(array)
def buscar(array):
    """
    Caso Coincidencia horizontal
    >>> array = np.array(([1, 2, 3, 4, 1], [4, 2, 3, 4, 2], [4, 2, 3, 4, 3], [2, 2, 3, 4, 2], [1, 2, 2, 4, 1]))
    >>> buscar(array)
    hay consecutivos en posicion(0)(0) y posicion final es:(0)(3)

    Caso sin coincidencia
    >>> array = np.array(([1, 2, 3, 2, 1], [4, 2, 3, 4, 2], [4, 2, 3, 4, 3], [2, 2, 3, 4, 2], [1, 2, 2, 4, 1]))
    >>> buscar(array)

    Caso coincidencia Vertical
    >>> array = np.array(([1, 2, 3, 2, 1], [4, 2, 3, 4, 2], [4, 2, 3, 4, 3], [2, 2, 3, 4, 4], [1, 2, 2, 4, 1]))
    >>> buscar(array)
    hay consecutivos en posicion(0)(4) y posicion final es:(3)(4)


    """
    for x in range(5):
        for y in range(5):
            if x < 2:
                if(array[x,y] == array[x+1,y]-1 and array[x,y] == array[x+2,y]-2 and array[x,y] == array[x+3,y]-3):
                    print("hay consecutivos en posicion("+str(x)+ ")("+str(y)+") y posicion final es:("+str(x+3)+")(" +str(y)+")")
            if y < 2:
                if(array[x,y] == array[x,y+1]-1 and array[x,y] == array[x,y+2]-2 and array[x,y] == array[x,y+3]-3):
                    print("hay consecutivos en posicion("+str(x)+")("+str(y)+ ") y posicion final es:("+str(x)+")(" +str(y+3)+")")



#Se genera un array 5 x 5 aleatorio para pruebas manuales

#array = np.random.randint(1,5,(5,5),int)
#buscar(array)


import doctest
doctest.testmod()



