import  matplotlib.pyplot as plt
import random
import numpy as np;
import math

def GEM(a,c,m,Xn1):


	#Ecuación: Xn = a(Xn-1+ c)mod m
	salida = np.array([])
	for i in range(10000):
		Xn = (a*Xn1+c) % m
		exponencial = (-5)* (math.log((Xn/m),math.e) )
		salida = np.append( salida , exponencial)
		Xn1 = Xn
	        
	return salida
	

	
#print( GEM(16807,0,2147483647,9))

pseudo = random.randint(1,9)


print(pseudo)

clases  = [ 0,1,2,3,4,5,6,7,8,9]

plt.hist ( GEM(16807,0,2147483647,pseudo) , clases , histtype= 'bar' , rwidth = 0.5 , color= 'pink')


plt.title('Histograma De Exponencial')
plt.xlabel(' clases ' )
plt.ylabel(' frecuencia ' )



plt.show()




