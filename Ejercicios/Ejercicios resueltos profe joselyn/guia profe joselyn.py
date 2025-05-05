
# cadena = input("Ingrese una cadena: ")

# repetidos = False

# for i in range(len(cadena) - 2):
#     # Aquí empieza un bucle for que recorre la cadena hasta 2 posiciones
#     # antes del final. Esto es para evitar que i+2 se salga del rango.
#     if cadena[1] == cadena[i+1] == cadena[i+2]:
#         repetidos = True

    



# if repetidos:
#     print("Sí, hay 3 caracteres seguidos iguales.")
# else:
#     print("No, no hay 3 caracteres seguidos iguales.")
# }




# Ingreso de un solo string con espacios entre nombres y apellidos
# entrada = input("Ingresa los 4 datos (primer nombre, segundo nombre, primer apellido, segundo apellido) separados por espacio:\n")

# # a) Separar en 4 variables distintas
# partes = entrada.split(" ")  # separa por espacios

# nombre1 = partes[0]
# nombre2 = partes[1]
# apellido1 = partes[2]
# apellido2 = partes[3]

# print("Primer nombre:", nombre1)
# print("Segundo nombre:", nombre2)
# print("Primer apellido:", apellido1)
# print("Segundo apellido:", apellido2)

# # b) Capitalizar la primera letra de cada uno
# nombre1 = nombre1.capitalize()
# nombre2 = nombre2.capitalize()
# apellido1 = apellido1.capitalize()
# apellido2 = apellido2.capitalize()

# print("\nCapitalizados:")
# print("Primer nombre:", nombre1)
# print("Segundo nombre:", nombre2)
# print("Primer apellido:", apellido1)
# print("Segundo apellido:", apellido2)

# # c) Intercalar letra por letra el primer nombre y el primer apellido


# intercalado = ""
# min_len = min(len(nombre1), len(apellido1))

# i = 0
# while i < min_len:
#     intercalado += nombre1[i] + apellido1[i]
#     i += 1

# # Agregar las letras restantes si alguno es más largo
# intercalado += nombre1[min_len:]
# intercalado += apellido1[min_len:]

# print("\nIntercalado (primer nombre + primer apellido):", intercalado)


precio_marraqueta = 2100  # precio por kg de marraqueta
precio_hallulla = 1900   # precio por kg de hallulla

total_marraqueta = 0
total_hallulla = 0

entrada = input("¿Desea comprar pan? (s/n): ").lower()

while entrada == "s":
    kilos = input("Ingrese los kilos: ")
    if kilos.replace('.', '', 1).isdigit():
        kilos = float(kilos)
        tipo = input("¿Qué pan desea \n1.-Marraqueta o \n2.-hallulla \n: ").lower()
        if tipo == "1":
            total_marraqueta += kilos
        elif tipo == "2":
            total_hallulla += kilos
        else:
            print("Tipo de pan no reconocido.")
    else:
        print("Por favor, ingrese un número válido.")
    
    entrada = input("¿Desea seguir comprando pan? (sí/no): ").lower()

total_pago = total_marraqueta * precio_marraqueta + total_hallulla * precio_hallulla

print("\nResumen de compra:")
print(f"Marraqueta: {total_marraqueta} kg")
print(f"Hallulla: {total_hallulla} kg")
print(f"Total a pagar: ${total_pago}")


