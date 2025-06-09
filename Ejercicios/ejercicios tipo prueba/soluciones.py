# Ejercicio 1: Filtrar y actualizar productos con bajo stock
def actualizar_precios(productos):
    actualizados = []
    for producto in productos:
        nuevo = producto.copy()
        if nuevo['stock'] < 5:
            nuevo['precio'] *= 1.15
        actualizados.append(nuevo)
    return actualizados

productos = [
    {"nombre": "Manzana", "precio": 100, "stock": 3},
    {"nombre": "Banana", "precio": 80, "stock": 6},
    {"nombre": "Pera", "precio": 120, "stock": 2}
]
print("# Ejercicio 1")
print(actualizar_precios(productos))


# Ejercicio 2: Contador de palabras en frases
import string
def contar_palabras(frases):
    conteo = {}
    for frase in frases:
        frase = frase.lower().translate(str.maketrans('', '', string.punctuation))
        for palabra in frase.split():
            conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

frases = ["Hola mundo", "hola, cómo estás mundo", "Mundo feliz"]
print("\n# Ejercicio 2")
print(contar_palabras(frases))


# Ejercicio 3: Promedio de alumnos y filtrado por nota
# Ejercicio 3: Promedio de alumnos y filtrado por nota (con promedio)
def filtrar_aprobados(estudiantes):
    aprobados = []
    for estudiante in estudiantes:
        promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
        if promedio > 6:
            aprobados.append({
                "nombre": estudiante["nombre"],
                "promedio": round(promedio, 2)
            })
    return aprobados

estudiantes = [
    {"nombre": "Ana", "notas": [7, 6, 8]},
    {"nombre": "Luis", "notas": [5, 5, 6]},
    {"nombre": "Carla", "notas": [9, 8, 10]}
]

print("\n# Ejercicio 3")
print(filtrar_aprobados(estudiantes))


# Ejercicio 4: Simulador de cajero automático
def cajero(monto, billetes_disponibles):
    resultado = {}
    for billete in sorted(billetes_disponibles, reverse=True):
        cantidad = monto // billete
        if cantidad:
            resultado[billete] = cantidad
            monto %= billete
    return resultado

monto = 385
billetes = [100, 50, 20, 10, 5]
print("\n# Ejercicio 4")
print(cajero(monto, billetes))


# Ejercicio 5: Estadísticas de ventas por producto
def estadisticas_ventas(ventas):
    totales = {}
    for venta in ventas:
        nombre = venta["producto"]
        cantidad = venta["cantidad"]
        totales[nombre] = totales.get(nombre, 0) + cantidad
    return totales

ventas = [
    {"producto": "Pan", "cantidad": 10},
    {"producto": "Leche", "cantidad": 5},
    {"producto": "Pan", "cantidad": 4},
    {"producto": "Jugo", "cantidad": 7}
]
print("\n# Ejercicio 5")
print(estadisticas_ventas(ventas))

