#Primer Ejercicio
import random as ran
def Aleatorio():
    a=ran.randint(100,120)
    return a
def Operation():
    c=0
    while c<10:
        a=Aleatorio()
        if a!= 110 and a!=115 and a!=119:
            if a%2==0 and c%2==0:
                print(a,"(PAR)")
                c+=1
            elif a%2!=0 and c%2!=0:
                print(a,"(IMPAR)")
                c+=1
        #else:                                                         #En el caso de estas líneas, son líneas de prueba en caso de ciclos infinitos, por lo tanto
        #    print(f"Número eliminado, se ha retornado el número {a}.")#si se eliminan los numerales, se ejecutarán sin problema alguno.
Operation()