#titulo: si puede votar o no

#entrada: se ingresa y determina una edad y nacionalidad como rango

#proceso: se establece la edad minima para votar siendo 18 y de nacionalidad colombiana, si se ingresa una edad menor a 18 y de otra nacionalidad no puede votar

#salida: se determina si la persona puede votar o no

edad =int(input("digite una edad"))
nacionalidad =str (input("digite su nacionalidad"))
if edad < 18 or nacionalidad !="colombiano":
    print ("usted no puede votar")
else:
    print ("usted puede votar")