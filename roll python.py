#titulo: determinar si el usuario tiene acceso o no

#entrada: se determina el rol de "admin" como ingreso para tener el acceso concedido

#proceso: al indicar el tipo de roll al sistema determinar si el usuario tiene el acceso concedido o denegado

#salida: determinar si tiene acceso concedido o denegado

rol1 = str(input("ingrese su rol:"))
if rol1 == "admin" :
    print ("acceso concedido")
else:
    print ("acceso denegado")