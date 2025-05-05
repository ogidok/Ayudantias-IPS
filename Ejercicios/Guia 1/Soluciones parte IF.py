# # Ejercicio 1: Número positivo, negativo o cero
# # Consigna:
# #  Pide al usuario un número e imprime si es positivo, negativo o cero.
# #  📌 Pista: Usa int(input()) para leer el número y condicionales if, elif, else para evaluarlo.
# # Salida esperada:
# # Ingresa un número: -3  
# # El número es negativo.


# try:
    
#     respuesta= int(input("Ingrese un numero: "))


#     if respuesta > 0:
#         print("El numero ingresado es positivo: ")
#     elif respuesta <0:
#         print("El numero ingresado es negativo.")
#     elif respuesta == 0:
#         print("El numero ingresado es neutro")
        
# except ValueError:
#     print("El numero ingresado no es un numero")
    


# Consigna: 
#  Solicita al usuario un año y determina si es bisiesto.
# 
# 📌 Pista: Un año es bisiesto si es divisible por 4, pero no por 100, salvo que también sea 
# divisible por 400


# anio = int(input("Ingresa un año:"))


# if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#     print(f"El año {anio} es biciesto.")
# else:
#     print(f"El año {anio} no es biciesto")
    
    


# num1= int(input("Ingresa el primer numero: "))
# num2= int(input("Ingresa el segundo numero: "))
# num3= int(input("Ingresa el tercer numero: "))

# mayor = min(num1,num2,num3)
# print(f"El numero mayor es {mayor}")


# num = int(input("Ingrese un numero: "))


# if num %2 ==0:
#     print(f"El numero {num} es par ")
# else:
#     print(f"El numero {num} es impar ")


# Ejercicio 5: Edad y acceso 
# Consigna: 
#  Solicita la edad del usuario y muestra si puede entrar a una fiesta
#  (mayores de 18).  📌 Pista: Usa una simple condición con >=.




# edad = input("Ingrese su edad: ")



# if edad < 18:
#     print("No puedes pasar.")
# else:
#     print("Puedes pasar.")





# import getpass

# paswd = getpass.getpass("Escribe algo: ")

# contraseña="1234567890okinacap"


# if paswd == paswd:
#     print("Acceso concedido")
# else:
#     print("Acceso denegado")





# Pista: IMC = peso / estatura^2. Usa float() y varias condiciones. Importa math si 
# deseas usar math.pow()


# peso = float(input("Ingrese su peso: "))
# estatura =float(input("Ingrese su estatura: "))



# imc=peso/estatura**2



# formula=



# if imc > 18.5:
#     print("EStas por debajo del peso normal")
# elif 18.5 <= imc < 25:
#     print("peso normal")
# elif 25 <= imc < 30:
#     print("sobrepeso")
# else:
#     print("Tienes obecidad")
    
# Consigna: 
#  Pide un número y verifica si está entre 1 y 100 (inclusive).  
#  📌 Pista: Usa operadores lógicos and para verificar el rango. 
# Salida esperada: 
# Ingresa un número: 45   
# El número está dentro del rango. 


# rango= list(range(0,101))



# num= int(input("Ingresa un numero: "))


# if num in rango:
#     print("Su numero esta en el rango ")
# else:
#     print("Su numero no esta en el rango")



# Consigna: 
#  Pide un número del 1 al 7 y muestra qué día de la semana representa.  
#  📌 Pista: Usa if o match-case si estás en Python 3.10+. 
# Salida esperada: 
# Ingresa un número (1-7): 5   
# # El día es: Viernes. 
 

# dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# indice= int(input("Ingresa un numero y te lo digo en dia de semana: "))

# menosuno= indice-1

# if 0 <= menosuno<len(dias_semana):
#     print(f"dia {indice} es : {dias_semana[menosuno]}")


# Ejercicio 10: Piedra, papel o tijera 
# Consigna: 
#  Simula el juego. Pide a dos jugadores que ingresen su elección y 
# determina el ganador.  📌 Pista: Usa varias condiciones if-elif para evaluar combinaciones. 
# Salida esperada: 
# Jugador 1, elige piedra, papel o tijera: piedra   
# Jugador 2, elige piedra, papel o tijera: tijera   
# Gana el Jugador 1.



# print("1: Piedra\n2: Papel\n3: Tijera")

# j1 = int(input("Jugador 1 elige (1-3): "))
# j2 = int(input("Jugador 2 elige (1-3): "))

# if j1 == j2:
#     print("Empate.")
# elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2):
#     print("Gana el Jugador 1.")
# elif (j2 == 1 and j1 == 3) or (j2 == 2 and j1 == 1) or (j2 == 3 and j1 == 2):
#     print("Gana el Jugador 2.")
# else:
#     print("Opción inválida.")7



# Consigna: 
#  Pide una palabra e imprímela al revés, letra por letra.  📌 Pista: Usa slicing [::-1] o reversed(). 
# Salida esperada: 

# *   


# Consigna: Pide una palabra e imprímela al revés, letra por letra en la misma línea usando for.

# palabra = input("Ingresa una palabra: ")

# for letra in palabra[::-1]:
#     print(letra, end="")




