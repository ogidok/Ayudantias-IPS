
# def sin_repetidos(lista):
#     listasinrepetidos=[]
#     for item in lista:
#         if item not in listasinrepetidos:
#             listasinrepetidos.append(item)

#     return listasinrepetidos

# print(sin_repetidos([1, 2, 2, 1, 4, 6, 2, 3, 4, 4, 1, 3] ))


# def asientos_disponibles(cine):
#     for fila in cine:
#         if "0" in fila:
#             return True
#     return False

# def porcentaje_disponible(cine):
#     total = 0
#     disponibles = 0
#     for fila in cine:
#         total += len(fila)
#         disponibles += fila.count("0")
#     if total == 0:
#         return 0
#     return (disponibles / total) * 100

# # Ejemplo de uso:
# cine = [
#     ["X","X","X","0","0"],
#     ["X","X","X","X","0"],
#     ["X","0","X","0","X"],
#     ["X","X","X","X","0"],
#     ["0","0","X","0","0"],
# ]

# print(asientos_disponibles(cine))
# print(porcentaje_disponible(cine))



# def mas_caro(productos):
#     producto = max(productos, key=lambda x: x[2])
#     return producto[1], producto[2]
# def mas_caro(productos):
#     max_precio = -1
#     producto_mas_caro = None
#     for producto in productos:
#         if producto[2] > max_precio:
#             max_precio = producto[2]
#             producto_mas_caro = producto
#     return producto_mas_caro[1], producto_mas_caro[2]


def bodega_stock(productos):
    total = 0
    for p in productos:
        total += p[3]
    return total


def obtener_precio(producto):
    return producto[2]

def mas_caro(productos):
    producto = max(productos, key=obtener_precio)
    return producto[1], producto[2]


productos = [
    (30144, 'Pendrive',7490,200), (65401, 'Audífonos',22500, 110),
    (68900, 'Teclado',3990,305), (21988, 'Mouse',8690, 178),
    (34560, 'Monitor',64990,15), (86899, 'Webcam',13990,10),
    (54544, 'Joystick', 41990, 100)
]

print(bodega_stock(productos))
print(mas_caro(productos))







