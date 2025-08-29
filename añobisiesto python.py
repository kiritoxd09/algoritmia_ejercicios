#titulo: año bisiesto

#entrada: ingresar un año en especifico

#proceso: recibe un numero y determina si es multiplo de 4 o no para indicar si el año es bisiesto o no

#salida: indicar que el año es bisiesto o no es bisiesto

año= int(input("digite un año:"))
if (año % 4 == 0 and año % 100 !=0) or (año & 400 == 0):
    print ("el año es bisiesto")
else:
    print ("el año no es bisiesto")