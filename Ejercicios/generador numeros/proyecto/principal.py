from numeros import generador_turno, decorador_turno
from random import *
def main():
    farmacia = generador_turno('F')
    perfumeria = generador_turno('P')
    cosmeticos = generador_turno('C')
    while True:
        area = input('Ingrese el área deseada (F, P, C): ').upper()
        if area == 'F':
            @decorador_turno
            def turno():
                print(next(farmacia))
            turno()
        elif area == 'P':
            @decorador_turno
            def turno():
                print(next(perfumeria))
            turno()
        elif area == 'C':
            @decorador_turno
            def turno():
                print(next(cosmeticos))
            turno()
        else:
            print('Área inválida')
        otro = input('¿Desea otro turno? (s/n): ')
        if otro != 's':
            break
        
if __name__ == '__main__':
    main()
