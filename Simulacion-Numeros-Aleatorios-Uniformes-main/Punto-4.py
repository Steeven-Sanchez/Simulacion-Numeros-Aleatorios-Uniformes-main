import numpy as np;
import math
from tabulate import tabulate

confianza = 0.5
n = 10000
clases =math.ceil ( math.sqrt (n) )


 
def generadorLinealCongruente(a,c,m,Xn1):

	#Ecuación: Xn = a(Xn-1+ c)mod m
	salida = np.array([])
	for i in range(n):
		Xn = (a*Xn1+c) % m
		salida =  np.append(salida, round(Xn/m,3))
		
		Xn1 = Xn
	
	return salida

p= generadorLinealCongruente(100,1234,165123,32)


a= 0
b= 0
c= 0
clase1=0
clase2=0
clase3=0
aux=0

j=0
for j in range(len(p)):
        i=0
        guarde_lista= []
        a = int ( p[j]*10)
        guarde_lista.append(a)
        b = int (  ( ( p[j]*10) - a)* 10)
        guarde_lista.append(b)
        c = int (  (  (    (   ( p[j]*10) - a) *10 ) - b ) * 10 )
        guarde_lista.append(c)
        k=0
    #Mechin voy a comentar mi parte poruqe no se que poner en la que usted hizo :v
        # ciclo while para recorrer el arreglo de 3 y saber cuantos digitos son iguales
        while k< len(guarde_lista):
                k=k+1
           #if para saber sí el primero y el segundo son iguales    
        if (guarde_lista[0]==guarde_lista[1]):
                        i= i +1
           #if para saber sí el primero y el ultimo son iguales            
        if (guarde_lista[0]==guarde_lista[2]):
                        i=i+1
             #if para saber sí el segundo y el ultimo son iguales              
        if (guarde_lista[1]==guarde_lista[2]):
                        i= i+1
         #Dependiendo del valor del contador asignamos el dato a una clase
        #clase 3 si ninguno es igual
        if (i== 0):
                clase3=clase3 + 1
         #clase 2 si dos de los datos son iguales       
        elif (1==i):
                clase2 = clase2 + 1
           #clase 1 si todos los datos son iguales     
        else: clase1= clase1 + 1
#calculamos el DM para la clase 1 teniendo en cuenta las probabilidades para un poker de
#con la formula (FE - FO)^2 / (FE)
Dm1= round((pow(((0.01*n) - clase1),2))/(0.01*n),4)

#calculamos el DM para la clase 2 teniendo en cuenta las probabilidades para un poker de

Dm2=round((pow(((0.27*n) -clase2),2))/(0.27*n),4)

#calculamos el DM para la clase 3 teniendo en cuenta las probabilidades para un poker de

Dm3=round((pow(((0.72*n) -clase3),2))/(0.72*n),4)

# se imprime la tabla con los datos obtenidos
tabla = [ [' clases ',' FO ', ' FE ', '(FE - FO)^2 / (FE)'],
             ['3 iguales',clase1, (0.01*n),Dm1],
             ['2 iguales',clase2, (0.27*n),Dm2],
             ['3 diferentes',clase3,round( (0.72*n),2),Dm3]]

        
print(tabulate(tabla))

#De calcula el DM total con la suma de los anterioromente calculados
DMcalculado = Dm1+Dm2+Dm3
#En la hipotesis se verifica si el DM calculado es menor al DM critico
#para saber si el generador es rechazado o no
#Para el tenemos 2 grados de libertad y una confianza del 5% el Dm critico es de 6
def hipotesis ():
	 
	if ( DMcalculado  <= 6 ):
		print ( "DMcalculado --> " , DMcalculado )
		print ( "DMcritico --> " , 6 )
		print ("R//  el generador no es rechazado")

	else:
		print ( "DMcalculado --> " , DMcalculado )
		print ( "DMcritico --> " , 6 )
		print ("R//  el generador es rechazado")
		

hipotesis()


    
