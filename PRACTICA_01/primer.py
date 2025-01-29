#4. Crear un archivo  .py  , escribir un Hola mundo que se imprima en consola. 
print("Hola, Mundo")

#5. Escribir un programa que salude con el nombre de entrada desde teclado 
Name=input("¿Cuál es tu nombre?: ")
print("Hola", Name)

#6. Escribe un programa que pida tu edad y muestre si es mayor de edad o no lo es.
Edad=int(input("¿Cuál es tu edad?: "))
if Edad >= 18:
    print("Ud. es mayor de edad")
else:
    print("Ud. es menor de edad")

#7. Escribe un programa que pida un numero entero y determine si es par o impar 
Num=int(input("Introduzca un número entero: "))
if Num % 2 == 0:
    print("El número brindado es par")
else:
    print("El número brindado es impar")

#8. Escribe un programa que que pida un numero entero y calcule la suma de 1 hasta el numero ingresado.
n=int(input("Introduzca un número entero: "))
formula=n*(n+1)/2
print("La suma total es igual a ",formula)
