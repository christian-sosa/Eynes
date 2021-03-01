import numpy as np

def CrearLista():
    lista = [dict(ID = str(x) , Edad = np.random.randint(100)) for x in range(10)]
    return lista 

def Criterio(lista):
    return lista['Edad']

def OrdenarLista(lista):
    lista.sort(reverse=True ,key=Criterio)
    print("ID de la persona mas joven: "+lista[9]['ID'])
    print("ID de la persona mas longeva: "+lista[0]['ID'])
    return lista

lista = CrearLista()
print(lista)
print(OrdenarLista(lista))
