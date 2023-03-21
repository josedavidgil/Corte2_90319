#Segundo Ejercicio
import math as mt
def F_matematica ():
    n=float(input("Ingrese el valor: "))
    f=input("Ingrese la función a aplicar (seno,coseno,tangente,exponencial,logaritmo natural): ")
    if f=="seno" or f=="Seno":
        print(f"El seno de {n} es {mt.sin(n)}")
    elif f=="coseno" or f=="Coseno":
        print(f"El coseno de {n} es {mt.cos(n)}")
    elif f=="tangente" or f=="Tangente":
        print(f"La tangente de {n} es {mt.tan(n)}")
    elif f=="exponencial" or f=="Exponencial":
        print(f"El exponencial de {n} es {mt.exp(n)}")
    elif f=="logaritmo natural" or f=="Logaritmo natural":
        print(f"El logaritmo natural de {n} es {mt.log(n)}")
    else:
        print("Por favor ingrese una función válida.")
        F_matematica()
F_matematica()