#titulo: examen aprobado o reprobado y si el estudiante aprueba o no

#entrada: ingresar un numero que va a ser determinado como nota

#proceso: al indicar un numero >= 60 el estudiante aprueba, de lo contrario reprueba

#salida: determinar si con la nota ingresada el estudiante aprueba o no

numero1 =float(input("ingrese la nota del examen:"))
if numero1>=60:
    print ("el estudiante aprobo")
else:
    print ("el estudiante reprobo")
