import sudoku
import random
from mapas import MAPAS
"""
Se entra por la funcion main en la cual se elige aleatoriamente
una representacion.La misma va ser representada en todas sus transformaciones
mediante la funcionm mostrar_sudoku(y sus subsecuentes funciones).
La funcion pedir_entrada va validar el input del usuario y le va dar el formato
para que ejecutar accion realize el comando solicitado.
El programa termina cuando el usuario usa la accion salir o cuando el sudoku
es completado
"""


def inicializar_sudoku(juego):
    valores_iniciales = []
    for fila in range(sudoku.ALTO_TABLERO):
        for celda in range(sudoku.ANCHO_TABLERO):
            if juego[fila][celda] != 0:
                valores_iniciales.append((fila,celda))
    return valores_iniciales

def imprimir_encabezado():
    print('')
    print(' '*9,'SUDOKU')
    LETRAS =('A','B','C','D','E','F','G','H','I')
    contador = 0
    print('\n')
    print('#',end=' ')
    for l in LETRAS:
        if contador == 3:
            print('#',end=' ')
            contador =0
        print(l,end=' ')
        contador += 1

def imprimir_separador():
    print('-'*25)

def mostrar_instrucciones():
    print('\n')
    print('-FORMATO PARA INGRESAR/REMPLAZAR/BORRAR (ACCION,FILACOLUMNA,VALOR) EJEMPLO:I,0A,2')
    print('-ACCIONES:')
    print('-INGRESAR/REMPLAZAR = I')
    print('-BORRAR = B')
    print('-SALIR = S,0A,0')
    print('-EVALUAR SI QUEDAN MOVIMIENTOS POSIBLES = H,0A,0')



def mostrar_sudoku(juego):
    contador_x = 0
    contador_y = 0
    imprimir_encabezado()
    print('\n')
    imprimir_separador()
    print('#',end=' ')
    for num,fila in enumerate(juego):
        if contador_y == 3:
            imprimir_separador()
            contador_y = 0
        for celda in fila:
            if contador_x == 3:
                print('#',end=' ')
                contador_x =0
            if celda==sudoku.VACIO:
                print('.',end=' ')
            else:
                print(celda,end=' ')
            contador_x += 1
        print('#',end=' ')
        print(f'({num})',end='')
        contador_y += 1
        print('\n')
    imprimir_separador()
    mostrar_instrucciones()




def pedir_entrada():
    validando = True
    CONV =('A','B','C','D','E','F','G','H','I')
    ACCIONES = ('I','B','S','H')
    while validando:
        ingreso = input("Ingrese valor: ")
        if len(ingreso.split(',')) != 3:
            print("ERROR DE INGRESO:FORMATO NO VALIDO,REINGRESAR")
            continue
        accion,coord,valor = ingreso.split(',')
        accion = accion.upper()
        if not(accion in ACCIONES):
            print("ERROR DE INGRESO:ACCION INCORRECTA")
            continue
        if valor.isdigit() and(int(valor)>=0) and(int(valor)<=9):
            valor=int(valor)
        else:
            print("ERROR DE INGRESO:VALOR INVALIDO")
            continue
        if (len(coord)== 2) and (coord[1].isalpha())and (coord[0].isdigit()):
            columna,fila = coord[1].upper(),int(coord[0])
            if not (columna in CONV):
                print("ERROR DE INGRESO:POSICION INVALIDA")
                continue
            columna = CONV.index(columna)
            coord = (fila,columna)
            break
        else:
            print("ERROR DE INGRESO:POSICION INVALIDA")
            continue
    return accion,coord,valor


def ejecutar_accion(accion,coordenadas,valor,juego,v_iniciales):
    fila,columna= coordenadas
    if accion == 'I':
        if (fila,columna) in v_iniciales:
            print('\n',"ERROR:VALOR INICIAL")
            return juego
        if not sudoku.es_movimiento_valido(juego, fila, columna, valor):
            print("\n","ERROR:El valor ingresado ya se encuentra en Fila/Columna/Region")
            return juego
        else:
            return sudoku.insertar_valor(juego, fila, columna, valor)

    if accion == 'B':
        if(fila,columna) in v_iniciales:
            print('\n',"ERROR:VALOR INICIAL")
            return juego
        return sudoku.borrar_valor(juego, fila, columna)

    if accion == 'S':
        print("\n","JUEGO FINALIZADO")
        return None
    if accion == 'H':
        if sudoku.hay_movimientos_posibles(juego):
            print('\n',"QUEDAN MOVIMIENTOS POSIBLES EN EL TABLERO")
        else:
            print('\n',"NO HAY MOVIMIENTOS POSIBLES")
        return juego




def main():
    representacion = MAPAS[random.randrange(0,50)]
    juego =sudoku.crear_juego(representacion)
    v_iniciales=inicializar_sudoku(juego)
    jugando = True
    v_ingresado = ''
    movimientos = 0

    while jugando:
        mostrar_sudoku(juego)
        accion,coordenadas,valor = pedir_entrada()
        juego= ejecutar_accion(accion,coordenadas,valor,juego,v_iniciales)
        if juego == None:
            print("\n","Juego Abandonado")
            print("\n","Movimientos totales: ",movimientos)
            break
        else:
            if sudoku.esta_terminado(juego):
                print("FELICITACIONES!!! JUEGO TERMINADO")
                print("Movimientos totales: ",movimientos)
                break
        movimientos += 1
    print('')
    input("Presione una tecla para continuar")



main()