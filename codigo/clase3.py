# 1. Solucionar la tarea
# 2. Condicionales (mas profundo)

"""
Escriba un programa en python que:
Pregunte al usuario si es intolerante a la lactosa, 
si es intolerante: pregunta si es alergico a los mariscos, 
si es alergico: imprime un mensaje diciendo que no tenemos platos para el. 
Si no es intolerante a la lactosa, se ofrece inmediatamente el postre de tres leches. 
Si es intolerante a la lactosa, pero no es alergico a los mariscos, 
se le ofrece una deliciosa cazuela de mariscos.
"""

# intolerante_a_lactosa = int(input("Usted es intolerante a la lactosa? (1= si, 2=no)"))

# if(intolerante_a_lactosa == 1):
#     alergico_a_mariscos = int(input("Usted es alergico a los mariscos? (1= si, 2=no)"))
#     if(alergico_a_mariscos == 1):
#         print("No tenemos platos para usted, perdon :(")
#     else:
#         print("Le podemos ofrecer la deliciosa cazuela de mariscos.")
# else:
#     print("Le podemos ofrecer el delicioso postre de tres leches")


"""
Escriba un programa en python que:
Pregunte dos numeros e imprima cual de ellos el el menor y cual es el mayor
"""

# numero2 = float(input("Por favor ingrese el primer numero"))
# numero1 = float(input("Por favor ingrese el segundo numero"))

# if( numero1 > numero2 ):
#     print(f"El numero mayor es: {numero1}")
#     print(f"El numero menor es: {numero2}")
# elif( numero1 != numero2 ):
#     print(f"El numero mayor es {numero2}")
#     print(f"El numero menor es {numero1}")
# else:
#     print("Ingreso dos numeros iguales")


"""
Escriba un programa en python que:
Pregunte dos numeros inicialmente, luego pregunte un tercer numero e imprima si el tercer numero esta
dentro del rango de los dos primeros.
"""

numero1 = float(input("Por favor ingrese el primer numero"))
numero2 = float(input("Por favor ingrese el segundo numero"))
numero3 = float(input("Por favor ingrese el tercer numero"))
# numero1 = 5
# numero2 = 1
# numero3 = 2
# temporal = 1

if (numero1>numero2):
    temporal=numero2
    numero2=numero1
    numero1=temporal
if( numero3 >= numero1 and numero3 <= numero2 ):
    print("esta dentro del rango")
else:
    print("NO esta dentro del rango")

