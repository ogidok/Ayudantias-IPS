# Resumen del Proyecto del Día 8
# Hoy aprendimos a escribir código más eficiente y mantenible mediante la instalación de paquetes, la modularización, el manejo de errores, las pruebas, decoradores y generadores.

# El desafío es desarrollar un turnero para una farmacia con tres áreas: perfumería, farmacia y cosméticos. El sistema asignará números de turno según el área elegida, llevándolos en secuencia (ejemplo: C-54 para cosmética). Luego, preguntará si se desea otro turno y repetirá el proceso.

# Pautas clave:
# Usar generadores para manejar los números de turno de manera eficiente.

# Utilizar decoradores para agregar un mensaje estándar antes y después del número de turno.

# Dividir el código en módulos:

# numeros.py: generadores y decorador.

# principal.py: lógica del programa e interacción con el usuario.

# El objetivo es aplicar todo lo aprendido para reforzar el conocimiento. Ahora, ¡a programar!

def decorador_turno(funcion):
    def decorar(*args,**kwargs):
        print('Turno:')
        funcion(*args,**kwargs)
        print('Gracias por su visita')
    return decorar
        
def generador_turno(area):
    turno=0
    for t in range(1,100):
        turno+=1
        yield f'{area}-{turno}'


