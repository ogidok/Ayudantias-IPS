# Recuerden que no hay una solucion pre establecida , mientras
# cumpla con las condiciones y salida esperada. Es valida.



# Ejercicio 1

# def sumanums(listanums):
#     suma=0
#     for num in listanums:
#         suma+=num

#     return suma

# # Ejemplo de uso
# print(sumanums([1,3,4,5]))
# #salida: 13


#Ejercicio 2

 
# def buscar_elemento(lista, valor):
#     for elemento in lista:
#         if elemento == valor:
#             return True  
#     return False  

# # Ejemplo de uso
# mi_lista = [3, 7, 1, 9, 5]
# print(buscar_elemento(mi_lista, 7))   # Salida: True
# print(buscar_elemento(mi_lista, 2))   # Salida: False


# Ejercicio 3
# def contar_vocales(lista):
#     vocales="aeiou"
#     contador=0
#     for item in lista:
#         item.lower()
#         for letra in item:
#             if letra in vocales:
#                 contador+=1
#             else:
#                 pass
#     return contador

# # # Ejemplo de uso
# print(contar_vocales(["dsdaj","dsgaghda"]))

# #Salida = 3




# #Ejercicio 4

# def filtrar_mayores(lista, umbral):
#     resultado = []
#     for numero in lista:
#         if numero > umbral:
#             resultado.append(numero)
#     return resultado
# # # # Ejemplo de uso
# print(filtrar_mayores([10, 3, 25, 8, 30], 10))
# # Salida esperada: [25, 30]



# #Ejercicio 5
# def invertir_lista(lista):
#     invertida = []
#     i = len(lista) - 1
#     while i >= 0:
#         invertida.append(lista[i])
#         i -= 1
#     return invertida

# # # # # Ejemplo de uso
# print(invertir_lista([1, 2, 3, 4, 5]))
# # Salida esperada: [5, 4, 3, 2, 1]



# #ejercicio 6
# def filtrar_primos(lista):
#     primos = []
#     for n in lista:
#         if n >= 2:
#             es_primo = True
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     es_primo = False
#                     break
#             if es_primo:
#                 primos.append(n)
#     return primos

# # # # # # Ejemplo de uso
# numeros = [1, 2, 3, 4, 5, 10, 11, 12, 13]
# print(filtrar_primos(numeros))
# #Salida esperada
# # [2, 3, 5, 11, 13]



# # #ejercicio 7
# def calcular_promedio(lista):
#     suma = 0
#     cantidad = 0
#     for numero in lista:
#         suma += numero
#         cantidad += 1
#     if cantidad == 0:
#         return 0  
#     return suma / cantidad

# # Ejemplo de uso
# numeros = [10, 20, 30, 40, 50]
# promedio = calcular_promedio(numeros)
# print("Promedio:", promedio)
# #Salida esperada:
# # Promedio: 30.0


# # # #ejercicio 8
# def eliminar_duplicados(lista):
#     resultado = []
#     for elemento in lista:
#         if elemento not in resultado:
#             resultado.append(elemento)
#     return resultado

# # # Ejemplo de uso
# lista_con_duplicados = [1, 2, 3, 2, 4, 1, 5, 3]
# lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)
# print(lista_sin_duplicados)
# #Salida esperada:
# # [1, 2, 3, 4, 5]

# # # #ejercicio 9

# def es_palindromo(palabra):
#     # Convertir a lista si es string
#     if isinstance(palabra, str):
#         lista = list(palabra)
#     else:
#         lista = palabra
    
#     i = 0
#     j = len(lista) - 1
    
#     while i < j:
#         if lista[i] != lista[j]:
#             return False
#         i += 1
#         j -= 1
#     return True

# # # # Ejemplo de uso y salidas esperadas
# print(es_palindromo("radar"))       # True
# print(es_palindromo(["a", "b", "b", "a"]))  # True
# print(es_palindromo("python"))      # False
