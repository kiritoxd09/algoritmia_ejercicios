#titulo: numero multiplo de cinco

#entrada: ingresar un numero como variable

#proceso: el numero ingresado sera calculado entre cinco lo cual determinara si es multiplo o no de cinco

#salida: indicar si el numero es multiplo de cinco o no

numero1 =float(input("ingrese un numero:"))
if numero1 % 5 == 0:
    print ("es numero multiplo de cinco")
else: 
    print("no es numero multiplo de cinco")