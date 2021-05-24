# Condicionales

# Tipo de variable booleana: True o False
# Operadores logicos: and, or, not
# Operadores relacionales: <, >, ==, <=, >=
# Palabras reservadas: if, else
# Tabla de verdad
# and: True and True = True
#      True and False = False
#      False and True = False
#      False and False = False
# or:  True or True = True
#      True or False = True
#      False or True = True
#      False or False = False

intolerante_a_lactosa = int(input("Usted es intolerante a la lactosa? (1= si, 2=no)"))
alergico_a_mariscos = bool(input("Usted es alergico a los mariscos? (1= si, 2=no)"))
# alergico_al_mani = bool(input("Usted es alergico al mani?"))


if (intolerante_a_lactosa == 2):
    print("Puede pedir el postre de tres leches")
else:
    print("No puede pedir el postre de tres leches")

if(alergico_a_mariscos==2):
    print("Puede pedir la cazuela de mariscos")
else:
    print("No puede pedir la cazuela de mariscos")


