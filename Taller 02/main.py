import pandas #Revisar librería para hacer el código mas facil
import csv
ar = pandas.read_csv('organization_data.csv')
ard_ord = ar.sort_values('Country', ascending=True)
ard_ord.to_csv('new_organization_data.csv', index=False)
paises = {}
with open('new_organization_data.csv') as file:
    lector_csv = csv.reader(file)
    next(lector_csv)
    for fila in lector_csv:
        pais = fila[4]
        if pais not in paises:
            paises[pais] = []
        paises[pais].append(fila)
print("Paises:")
for i, pais in enumerate(paises.keys()):
    print(f"{i+1}. {pais}")
num_pais = int(input("Ingrese el número del país a solicitar: "))

paisso= list(paises.keys())[num_pais - 1]
print(f"Usted seleccionó el país: {paisso}")
empresas = []
with open('new_organization_data.csv') as file:
    lector_csv = csv.reader(file)
    next(lector_csv)
    for fila in lector_csv:
        pais = fila[4]
        if pais == paisso:
            empresas.append(fila)
mayor_empresa = None
mayor_empleados = 0
for empresa in empresas:
    num_empleados = int(empresa[8])
    if num_empleados > mayor_empleados:
        mayor_empleados = num_empleados
        mayor_empresa = empresa

print(f"La empresa con más empleados en {paisso} es {mayor_empresa[2]}")
print(f"Sitio web: {mayor_empresa[3]}")
print(f"Descripción: {mayor_empresa[5]}")
print(f"Fundación: {mayor_empresa[6]}")
print(f"Industria: {mayor_empresa[7]}")
print(f"Empleados: {mayor_empleados}")

menor_empresa = None
menor_empleados = float('inf')
for empresa in empresas:
    num_empleados = int(empresa[8])
    if num_empleados < menor_empleados:
        menor_empleados = num_empleados
        menor_empresa = empresa

print(f"La empresa con menos empleados en {paisso} es {menor_empresa[2]} ")
print(f"Website: {menor_empresa[3]}")
print(f"Descripción: {menor_empresa[5]}")
print(f"Fundación: {menor_empresa[6]}")
print(f"Industria: {menor_empresa[7]}")
print(f"#Empleados {menor_empleados}")

total_empleados = 0
num_empresas = len(empresas)
for empresa in empresas:
    num_empleados = int(empresa[8])
    total_empleados += num_empleados
promedio_empleados = total_empleados / num_empresas
print(f"El promedio de empleados en {paisso} es {promedio_empleados:.2f}.")
num_empresas = len(empresas)
print(f"Cantidad de empresas en {paisso}: {num_empresas}")