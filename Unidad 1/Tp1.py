##1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")
##2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
##el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
##por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
##realizar la impresión por pantalla

nombre = input("¿Tu nombre? ")
print(f"Hola {nombre}")

##3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
##imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
##“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
##años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
##la impresión por pantalla.

nombre = input("¿Tu nombre? ")
apellido = input("¿Tu apellido? ")
edad = input("¿Tu edad? ")
lugar = input("¿Tu lugar de residencia? ")  
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

## 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
##su perímetro.
radio = float(input("Radio del círculo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área es: {area}")    
print(f"El perímetro es: {perimetro}")

##5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
##cuántas horas equivale.
segundos = int(input("Cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas} horas")
##6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
##multiplicar de dicho número. 
numero = int(input("Número: ")) 
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

## 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
##pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: ")) 
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")  
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

## 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
##de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
##modo:
##𝐼𝑀𝐶 =
##𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
##(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura = float(input("Altura (m): "))
peso = float(input("Peso (kg): "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {imc}")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =
9
5
. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32"""

celsius = float(input("Temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32   
print(f"Equivale a {fahrenheit} grados Fahrenheit")

"""10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))   
num3 = float(input("Número 3: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")


