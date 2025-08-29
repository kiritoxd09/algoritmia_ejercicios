#titulo: temperatura apropiada para congelar

#entrada: el numero ingresado sera la medido como "temperatura"

#proceso: el numero se calculara como mayor o menor siendo menor "suficiente" y mayor como "no suficiente" 
 
#salida: se determinara si la temperatura ingresada es adecuada para congelar o no

numero1 =float (input("ingrese la temperatura:"))
if numero1>= 1:
    print ("la temperatura no es suficiente para congelar")
else:
    print ("la temperatura es suficiente para congelar")