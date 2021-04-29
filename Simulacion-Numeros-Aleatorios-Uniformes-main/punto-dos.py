import numpy as np
import random
import  matplotlib.pyplot as plt



# creamos un vector  con rango entre 1 y 99
# dividimos este ventor entre 100 para que quede  U [0,1)


#se generan un arreglo de 1000 datos entre [0 , 1)
vet = (np.random.randint(1, 99 , 1000 )/ 100)

# arreglo para graficar el histograma
z= [ 1 ,3 ,5, 7, 9, 11, 13]

#Funcion para transformar la distribución discreta 
def transformar (lista):
    
    a = [ 1 ,3 ,5, 7, 9, 11 ]
    pa = [0.2 ,0.35 ,0.5 , 0.6 , 0.85 , 1.0 ]
    new_list= []
    i=0 
    while   i < len(lista)  :

          

          if (lista[i]<pa[0]) :
                new_list.append(a[0])

          elif ( (lista[i]>pa[0])and(lista[i]<pa[1]) )  : 
                 new_list.append(a[1])
          
          elif ( (lista[i]>pa[1]) and(lista[i]<pa[2]) )  : 
                  new_list.append(a[2])
          
          elif ( (lista[i]>pa[2]) and(lista[i]<pa[3]) )  : 
                  new_list.append(a[3])
          
          elif ( (lista[i]>pa[3]) and(lista[i]<pa[4]) )  : 
                  new_list.append(a[4])

          else :
               new_list.append(a[5])

          i= i+1     

          

    return new_list

# Funcion para mostrar los datos de r y su transformada a en forma de

def tabla (v,l) :

    i=0
    print ( ' {:^10}{:^10}' . format( ' r ',  ' a ' ) )
    while i < len(v) :
            
            print('{:^10}{:^10}' .format(v[i],l[i]))
            i = i+1       

elements = [ 1 , 3 , 5, 7 , 9 , 11]
probabilities = [ 0.2 , 0.15 , 0.15 , 0.1 , 0.25 , 0.15 ]
#Generar 100 numeros bajo esta distribución
n = 1000
# Se generan 1000 datos de forma aleatoria teniendo en cuenta la probabilidad
numbers = np.random.choice ( elements , n , p=probabilities )


#descomentar para ver histograma del codigo del taller 

# se genera el histograma del generador de números mediante probabilidades
#plt.hist ( numbers , z, histtype= 'bar' , rwidth = 0.3, color= 'red' )
#plt.title ( "Histograma generador implementado mediante probabilidedes" )


lista_transformada = transformar(vet)

print(  tabla(vet , lista_transformada ))

#se genera el histograma de la trasnformación discreta
plt.hist ( (lista_transformada) ,z, histtype= 'bar' , rwidth = 0.3, color= 'blue')
plt.title("Histograma De Transformación Discreta" )
plt.xlabel(' clases ' )
plt.ylabel(' frecuencia ' )
plt.show()
