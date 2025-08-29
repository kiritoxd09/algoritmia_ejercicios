#titulo: triangulo escaleno,isoceles o equilatero

#entrada: ingresar tres numeros que se determinan como lados

#proceso: al indicar con un numero los 3 lados del tringulo determinar que tipo es

#salida: determinar si el triangulo es escaleno,isoceles o equilatero

num1=float(input("ingrese el lado 1:"))
num2=float(input("ingrese el lado 2:"))
num3=float(input("ingrese el lado 3:"))
if num1 == num2 and num2 == num3:
    print ("el triangulo es equilatero")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print ("el triangulo es isoceles")
else:
    print ("el triangulo es escaleno")