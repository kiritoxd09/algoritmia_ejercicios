#titulo: ingresar contraseña 

#entrada: ingresar la contraseña establecida para determinar si es correcta o no

#proceso: se establece la contraseña y se ingresa para mostrar si es la indicada o no

#salida: se determina si la contraseña es correcta o no 

clave1= str(input("ingrese su contraseña:"))
if clave1 == "pasword" :
    print ("contraseña correcta")
else: 
    print ("contraseña incorrecta")