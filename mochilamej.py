## CREADO Versión inicial NDD Sept 2020
## Modificaciones posteriores

import random
import numpy as np


"""   Comentarios son Una Linea: #
O triple comilla doble: Un bloque"""

"""Si se desea una población inicial no aleatoria
"""

cromosoma1 = [1, 0, 0, 1]
cromosoma2 = [1, 1, 0, 0]
cromosoma3 = [0, 1, 1, 0]
cromosoma4 = [0, 0, 1, 0]
poblInicial = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4])


# MEJORA: Tamaño de la Población como parametro
#random.seed(1)
#print("\n","aletorio:", random.randrange(2)) #Entero 0 o 1

##### FUNCIONES PARA OPERADORES


def evalua(n,x,poblIt,utilidad,pesos):
    suma=0
    sumaPesos=0
    total=0
    for i in range(0, n):
      for j in range(0,x):
        suma+=poblIt[i,j]*utilidad[j]
        sumaPesos+=poblIt[i,j]*pesos[j]
      fitness[i]=suma
      ValoresPesos[i]=sumaPesos
      total+=suma
      suma=0
      sumaPesos=0
    return fitness,total,ValoresPesos

def imprime(n,total,fitness,poblIt,ValoresPesos):
    #Tabla de evaluación de la Población
    acumula=0
    print ("\n",'Tabla Iteración:',"\n")
    for i in range(0, n):
      probab=fitness[i]/total
      acumula+=probab
      print([i+1]," ",poblIt[i],"  ",fitness[i]," ","{0:.1f}".format(ValoresPesos[i])," ","{0:.3f}".format(probab)," ","{0:.3f}".format(acumula))
      acumulado[i]=acumula
    print("Total Fitness:      ", total)
    return acumulado

def seleccion(acumulado):
    escoje=np.random.rand()
    print("escoje:      ", escoje)

    for i in range(0,n):
      if acumulado[i]>escoje:
         padre=poblIt[i]
         break
    return (padre)


def cruce(a1,p1,p2):
    if a1<Pcruce:
      print("Mas grande", Pcruce, "que ", a1, "-> Si Cruzan")
      puntoCorte=np.random.rand()
      print("punto corte: ",puntoCorte)
      Corte = 1/(x-1)  # cada 1/(x-1) hay punto de corte
      i=1
      pos=0
      for i in range(x):
         if i*Corte > puntoCorte:
            pos=i
            break
      print('\nEl corte es en la posicion', pos)
      temp1=p1[0:pos] #[i:j] corta desde [i a j)
      temp2=p1[pos:x]
      print(temp1,temp2)
      temp3=p2[0:pos]
      temp4=p2[pos:x]
      print(temp3,temp4)
      hijo1 = list(temp1)
      hijo1.extend(list(temp4))
      hijo2 = list(temp3)
      hijo2.extend(list(temp2))

    else:
      print("Menor", Pcruce, "que ", a1, "-> NO Cruzan")
      hijo1=p1
      hijo2=p2

    return hijo1,hijo2

def mutacion(hijo):
  print("Mutacion")
  pos=1
  for i in hijo:
    ran=np.random.rand()
    print("gen ",pos,"random: ",ran )
    if(ran<=Pmuta):
      print("cambia")
      if i == 0:
        i=1
        hijo[pos-1]=i
      else:
        i=0
        hijo[pos-1]=i
    pos=pos+1
  return hijo

def verificarHijo (hijo,pesos):
  sumaPesos = 0
  for j in range(x):
    sumaPesos+=hijo[j]*pesos[j]
  return sumaPesos





#### Parametros #####
x=4  #numero de variables de decision - Elementos diferentes: x
n=4  #numero de individuos en la poblacion - cromosomas: n
Pcruce=0.98  #Probabilidad de Cruce
Pmuta=0.1   #Probabilidad de Mutación


fitness= np.empty((n))
ValoresPesos= np.empty((n))
acumulado= np.empty((n))
suma=0
total=0

#Individuos, soluciones o cromosomas
#poblInicial = np.random.randint(0, 2, (n, x)) # aleatorios (n por x) enteros entre [0 y2)
#random.random((4,5)) # 4 individuos 5 genes

# Ingresar los datos del Problema de la Mochila - Peso y Utilidad de los Elementos
pesos = [7, 6, 8, 2 ]
utilidad = [4, 5, 6, 3 ]
#pesos = [5, 7, 10, 30, 25]
#utilidad = [10, 20, 15, 30,15]

print("Poblacion inicial:","\n", poblInicial)
print("\n","Utilidad:", utilidad)
print("\n","Pesos", pesos )
poblIt=poblInicial

######  FIN DE LOS DATOS INICIALES



##Llama función evalua, para calcular el fitness de cada individuo
fitness,total,ValoresPesos=evalua(n,x,poblIt,utilidad,pesos)
#####print("\n","Funcion Fitness por individuos",  fitness)
#####print("\n","Suma fitness: ",  total)

##### imprime la tabla de la iteracion
imprime(n,total,fitness,poblIt,ValoresPesos)

##### *************
# Inicia Iteraciones

# Crear vector de 5x2 vacio  a = numpy.zeros(shape=(5,2))
numeroIteraciones = input("Ingresa la cantidad de iteraciones deseada: ")
for iter in range(int(numeroIteraciones)):
  print("\n","iteración ", iter+1)
  hijosVivos=0
  i=0
  while hijosVivos<n:

    papa1=seleccion(acumulado) # Padre 1
    print("padre 1:", papa1)
    papa2=seleccion(acumulado) # Padre 2
    print("padre 2:", papa2)
    print("Cruce")
    hijoA,hijoB=cruce(np.random.rand(),papa1,papa2)
    print("hijo1: ", hijoA)
    print("hijo2: ", hijoB)
    print("Mutacion")
    hijoA=mutacion(hijoA)
    hijoB=mutacion(hijoB)
    print("hijo1: ", hijoA)
    print("hijo2: ", hijoB)
    print("Vive o muere")
    PesosHA = verificarHijo(hijoA,pesos)
    PesosHB = verificarHijo(hijoB,pesos)
    if PesosHA<=15 and hijosVivos<n:
      poblIt[i]=hijoA
      i+=1
      print("Peso hijo 1: ",PesosHA, "VIVE")
      hijosVivos+=1
    else:
      print("Peso hijo 1: ",PesosHA, "MUERE")
    if PesosHB<=15 and hijosVivos<n:
      poblIt[i]=hijoB
      i+=1
      print("Peso hijo 2: ",PesosHB, "VIVE")
      hijosVivos+=1
    else:
      print("Peso hijo 2: ",PesosHB, "MUERE")
    print("Cantidad de hijos vivos: ",hijosVivos)





  print("\n","Poblacion Iteración ", iter+1,"\n", poblIt)
  fitness,total,ValoresPesos=evalua(n,x,poblIt,utilidad,pesos)
  #### print("\n","Funcion Fitness por individuos",  fitness)
  #### print("\n","Suma fitness: ",  total)

  ##### imprime la tabla de la iteracion
  imprime(n,total,fitness,poblIt,ValoresPesos)