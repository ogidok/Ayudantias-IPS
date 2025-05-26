# # Ejercicio 1

# def sumar_valores(diccionario):
#     suma = 0
#     for valor in diccionario.values():
#         suma += valor
#     return suma

# # Ejemplo de uso
# print(sumar_valores({"a": 1, "b": 2, "c": 3}))
# # salida: 6

# Ejercicio 2

# def buscar_clave(diccionario, clave):
#     return clave in diccionario

# # Ejemplo de uso
# print(buscar_clave({"a": 1, "b": 2}, "a"))
# # salida: True

# # Ejercicio 3

# def contar_valor(diccionario, valor_buscar):
#     contador = 0
#     for valor in diccionario.values():
#         if valor == valor_buscar:
#             contador += 1
#     return contador

# # Ejemplo de uso
# print(contar_valor({"a": 1, "b": 2, "c": 1}, 1))
# # salida: 2


# Ejercicio 4

# def filtrar_mayores(diccionario, umbral):
#     resultado = {}
#     for clave, valor in diccionario.items():
#         if valor > umbral:
#             resultado[clave] = valor
#     return resultado

# # Ejemplo de uso
# print(filtrar_mayores({"a": 3, "b": 7, "c": 2}, 4))
# # salida: {'b': 7}


# Ejercicio 5

# def invertir_diccionario(diccionario):
#     invertido = {}
#     for clave, valor in diccionario.items():
#         invertido[valor] = clave
#     return invertido

# # Ejemplo de uso
# print(invertir_diccionario({"a": 1, "b": 2}))
# # salida: {1: 'a', 2: 'b'}


# Ejercicio 6

# def contar_prefijo(diccionario, prefijo):
#     contador = 0
#     for clave in diccionario:
#         if clave.startswith(prefijo):
#             contador += 1
#     return contador

# # Ejemplo de uso
# print(contar_prefijo({"pre1": 10, "pre2": 20, "otra": 30}, "pre"))
# # salida: 2


# Ejercicio 7

# def clave_valor_maximo(diccionario):
#     return max(diccionario, key=diccionario.get)

# # Ejemplo de uso
# print(clave_valor_maximo({"a": 5, "b": 12, "c": 8}))
# # salida: 'b'

# Ejercicio 8

# def eliminar_nulos(diccionario):
#     limpio = {}
#     for clave, valor in diccionario.items():
#         if valor not in (None, "", 0):
#             limpio[clave] = valor
#     return limpio

# # Ejemplo de uso
# print(eliminar_nulos({"a": 1, "b": 0, "c": "", "d": None, "e": 5}))
# # salida: {'a': 1, 'e': 5}



# Ejercicio 9

# def combinar_diccionarios(dic1, dic2):
#     combinado = dic1.copy()
#     for clave, valor in dic2.items():
#         if clave in combinado:
#             combinado[clave] += valor
#         else:
#             combinado[clave] = valor
#     return combinado

# # Ejemplo de uso
# print(combinar_diccionarios({"a": 1, "b": 2}, {"b": 3, "c": 4}))
# # salida: {'a': 1, 'b': 5, 'c': 4}
