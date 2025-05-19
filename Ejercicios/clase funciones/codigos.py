
# def suma(*args):
#     resultado = 0
#     for numero in args:
#         resultado += numero
#     return resultado

# # Ejemplos:
# print(suma(1, 2))            # 3
# print(suma(1, 2, 3, 4, 5))   # 15
# print(suma())                # 0



# def suma_cuadrados(*args):
#     return sum(x**2 for x in args)

# resultado = suma_cuadrados(1, 2, 3)
# print(resultado)  # Salida: 14 (1² + 2² + 3²)



# def numeros_persona(nombre,*args):
#     suma =0
#     for n in args:
#         suma+=n
#     return f"Hola {nombre} la suma de tus numeros es {suma}"

# print(numeros_persona("Diego",1,2,3))
# #salida esperada
# #Hola Diego la suma de tus numeros es 6


# def mostrar_info(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# # Ejemplo:
# mostrar_info(nombre="Juan", edad=30, ciudad="Santiago")
# #salida
# # nombre: Juan
# # edad: 30
# # ciudad: Santiago

# print(cantidad_atributos(1, 2, 3))  # Salida: 3
# print(cantidad_atributos(nombre="Juan", edad=30))  # Salida: 2
# print(cantidad_atributos(1, 2, nombre="Juan"))  # Salida: 3


# print(lista_atributos(nombre="Ana", edad=25, ciudad="Santiago"))
# # Salida: ['Ana', 25, 'Santiago']

# print(lista_atributos())  
# # Salida: []


# ...
# Ejemplo:
# describir_persona("María", color_ojos="azules", color_pelo="rubio")

# #salida esperada
# Características de {nombre}:
# {clave1}: {valor1}
# {clave2}: {valor2}