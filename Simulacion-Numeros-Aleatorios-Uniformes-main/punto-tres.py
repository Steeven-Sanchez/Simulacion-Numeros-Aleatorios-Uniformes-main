#encoding: utf-8
#Autor: Carlos A Delgado S
#Fecha: 03 de Junio de 2019
import numpy as np;
import math 

#Esta función implementar el generador lineal congruente

confianza = 0.5
n = 10000
clases =math.ceil ( math.sqrt (n) )
DMcritico= 1.36 / math.sqrt(n)

def generadorLinealCongruente(a,c,m,Xn1):

	#Ecuación: Xn = a(Xn-1+ c)mod m
	salida = np.array([])
	for i in range(n):
		Xn = (a*Xn1+c) % m
		salida =  np.append(salida, (Xn/m))
		
		Xn1 = Xn
	
	return salida
	
GLC=generadorLinealCongruente(100,1234,165123,32)

#print (clases)

aux=0
FO =[]
array_clases = [ [ ]  ]

for i in range(clases):

   a= aux
   b= (i+1)/clases
   
   array_clases =  [  a , b ]
   #print (array_clases )
   j=0
   sumele=0
   while j < len(GLC):
	   
	   
	   
	   if ( ( GLC [ j ] >= a ) and ( GLC[j]<  b) ):
	   
	                 sumele = sumele+1
	   j= j+1
	   
   FO.append(sumele)               
		    
   
   aux = b
   
def tabla (v) :
    FOA =0
    FE = 0
    POA=0
    PEA = 0
    i=0
    mayor = 0
    print ( '{:^10} {:^10}{:^10}{:^10}{:^10}{:^10}' . format('        Clases        ', '            FO ', '           FOA', '        POA ', '          PEA' ,   '         PEA - POA') )
    while i < len(v) :
            
            rango = PEA	    
            FOA = FOA + FO[i]
            FE = FE+ (1/clases)
            POA = POA + FO[i]
            PEA = PEA + (1/clases)
            dm =abs(PEA - (POA/n) )
          
            
            print ( ' {:^10.4f}{:^10.4f}{:^20.4f}{:^5.4f}{:^15.4f}{:^10.4f}{:^20.4f}' . format(rango,  PEA,  FO[i],FOA,(POA/n),PEA,dm))
            i = i+1
            
            if (mayor < dm): mayor = dm
	 
		    	     
    return mayor



#print (tabla(FO) )          
#print (array_clases)
#print (generadorLinealCongruente(100,1234,165123,32))
#print ( FO )

def hipotesis ():
	DMcalculado = tabla(FO) 
	if ( DMcalculado  <= DMcritico ):
		print ( "DMcalculado --> " , DMcalculado )
		print ( "DMcritico --> " , DMcritico )
		print ("R//  el generador no es rechazado")

	else:
		print ( "DMcalculado --> " , DMcalculado )
		print ( "DMcritico --> " , DMcritico )
		print ("R//  el generador es rechazado")
		

hipotesis()
