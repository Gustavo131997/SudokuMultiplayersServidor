# -*- coding: cp1252 -*-
import random


def RellenaCuadrante(tabla, cuadrante=1):
    filas = len(tabla)
    columnas = len(tabla[0])
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    minifilas = RetornaMinifilas(tabla, cuadrante)
    minicolumnas = RetornaMinicolumnas(tabla, cuadrante)
    for i in minifilas:
        for j in minicolumnas:
            longitud = len(disponibles)
            aleatorio = random.randint(0, longitud - 1)
            tabla[i][j] = disponibles[aleatorio]
            disponibles.remove(disponibles[aleatorio])


def CreaTablaBlanco():
    return [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def IntroducirValoresTabla(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    print "Vamos a introducir los valores del sudoku para llenar la tabla"
    print "Indtroduzca los valores de izquierda a derecha y de arriba a bajo"
    print "En las casillas sin valor introduzca un 0"
    filasentrada = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        while len(filasentrada[i]) != 9:
            print"Introduzca los valores de la fila", i + 1,
            filasentrada[i] = raw_input()
    for i in range(filas):
        for j in range(columnas):
            tabla[i][j] = int(filasentrada[i][j])


def VisualizaTabla(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        if i == 0 or i == 3 or i == 6: print "- - - - - - - - - - - - -"
        for j in range(columnas):
            if j == 0 or j == 3 or j == 6: print "|",
            print tabla[i][j],
            if j == 8: print"|"
        if i == 8: print "- - - - - - - - - - - - -"
        # print "\n"


def CuentaCeros(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    ceros = 0
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:
                ceros += 1
    return ceros


def RetornaMinifilas(tabla, cuadrante):
    if cuadrante == 1 or cuadrante == 2 or cuadrante == 3:
        return [0, 1, 2]
    elif cuadrante == 4 or cuadrante == 5 or cuadrante == 6:
        return [3, 4, 5]
    elif cuadrante == 7 or cuadrante == 8 or cuadrante == 9:
        return [6, 7, 8]


def RetornaMinicolumnas(tabla, cuadrante):
    if cuadrante == 1 or cuadrante == 4 or cuadrante == 7:
        return [0, 1, 2]
    elif cuadrante == 2 or cuadrante == 5 or cuadrante == 8:
        return [3, 4, 5]
    elif cuadrante == 3 or cuadrante == 6 or cuadrante == 9:
        return [6, 7, 8]


def RetornaCuadrante(fila, columna):
    if fila <= 2 and columna <= 2:
        return 1
    elif fila <= 5 and columna <= 2:
        return 4
    elif fila <= 8 and columna <= 2:
        return 7
    elif fila <= 2 and columna <= 5:
        return 2
    elif fila <= 5 and columna <= 5:
        return 5
    elif fila <= 8 and columna <= 5:
        return 8
    elif fila <= 2 and columna <= 8:
        return 3
    elif fila <= 5 and columna <= 8:
        return 6
    elif fila <= 8 and columna <= 8:
        return 9


def RetornaPosiblesVertical(tabla, fila, columna):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    filas = len(tabla)
    for i in range(filas):
        if i != fila:
            valor = tabla[i][columna]  # valor que hay asignado
            if valor in disponibles:  # si el valor que hemos leido esta en la lista
                disponibles.remove(valor)  # lo borramos de la lista ya que no disponible
    return disponibles


def RetornaPosiblesHorizontal(tabla, fila, columna):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    columnas = len(tabla[0])
    for i in range(columnas):
        if i != columna:
            valor = tabla[fila][i]  # valor que hay asignado
            if valor in disponibles:  # si el valor que hemos leido esta en la lista
                disponibles.remove(valor)  # lo borramos de la lista ya que no disponible
    return disponibles


def RetornaPosiblesCuadrante(tabla, fila, columna):
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cuadrante = RetornaCuadrante(fila, columna)
    minifilas = RetornaMinifilas(tabla, cuadrante)
    minicolumnas = RetornaMinicolumnas(tabla, cuadrante)
    valorinicialenpuntoestudio = tabla[fila][columna]
    tabla[fila][columna] = 'estudio'
    for i in minifilas:
        for j in minicolumnas:
            if tabla[i][j] != 'estudio':
                valor = tabla[i][j]
                if valor in disponibles:
                    disponibles.remove(valor)
    tabla[fila][columna] = valorinicialenpuntoestudio  # volvemos a poner el valor inicial
    return disponibles


def RetornaInvertidos(posibles):
    imposibles = []
    if not (1 in posibles):
        imposibles.append(1)
    if not (2 in posibles):
        imposibles.append(2)
    if not (3 in posibles):
        imposibles.append(3)
    if not (4 in posibles):
        imposibles.append(4)
    if not (5 in posibles):
        imposibles.append(5)
    if not (6 in posibles):
        imposibles.append(6)
    if not (7 in posibles):
        imposibles.append(7)
    if not (8 in posibles):
        imposibles.append(8)
    if not (9 in posibles):
        imposibles.append(9)
    return imposibles


def RetornaTotalPosibles(tabla, fila, columna):
    lista1 = RetornaPosiblesVertical(tabla, fila, columna)
    lista2 = RetornaPosiblesHorizontal(tabla, fila, columna)
    lista3 = RetornaPosiblesCuadrante(tabla, fila, columna)
    lista1 = RetornaInvertidos(lista1)
    lista2 = RetornaInvertidos(lista2)
    lista3 = RetornaInvertidos(lista3)
    listatotal = lista1 + lista2 + lista3
    listaimposibles = []
    if 1 in listatotal:
        listaimposibles.append(1)
    if 2 in listatotal:
        listaimposibles.append(2)
    if 3 in listatotal:
        listaimposibles.append(3)
    if 4 in listatotal:
        listaimposibles.append(4)
    if 5 in listatotal:
        listaimposibles.append(5)
    if 6 in listatotal:
        listaimposibles.append(6)
    if 7 in listatotal:
        listaimposibles.append(7)
    if 8 in listatotal:
        listaimposibles.append(8)
    if 9 in listatotal:
        listaimposibles.append(9)
    listaposibles = RetornaInvertidos(listaimposibles)
    return listaposibles


def CompruebaTerminado(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        valor = 0
        for j in range(columnas):
            valor += tabla[i][j]
        print "La suma de columna=", i, "es de", valor
    for j in range(columnas):
        valor = 0
        for i in range(filas):
            valor += tabla[i][j]
        print "La suma de fila=", i, "es de", valor


def RellenaInmediatos(tabla):
    actuado = 0
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 1:
                    tabla[i][j] = posibles[0]
                    actuado = 1
    return actuado


def RetornaUnoDeLaLista(lista):
    longitud = len(lista)
    return lista[random.randint(0, longitud - 1)]


def RellenaUnaCasillaCon2Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 2:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return 1
    return 0


def RellenaUnaCasillaCon3Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 3:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return 1
    return 0


def RellenaUnaCasillaCon4Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 4:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return 1
    return 0


def RellenaUnaCasillaCon5Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 5:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return 1
    return 0


def RellenaUnaCasillaCon6Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 6:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return 1
    return 0


def RellenaUnaCasillaCon7Posibles(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    for i in range(filas):
        for j in range(columnas):
            if tabla[i][j] == 0:  # casilla vacia
                posibles = RetornaTotalPosibles(tabla, i, j)
                if len(posibles) == 7:
                    tabla[i][j] = RetornaUnoDeLaLista(posibles)
                    return 1
    return 0


def RellenaPosibilidades(tabla):
    filas = len(tabla)
    columnas = len(tabla[0])
    contador = 0
    while CuentaCeros(tabla) != 0 and contador <= 200:
        contador += 1
        while RellenaInmediatos(tabla) == 1:
            print "rellenada inmediatos"
            # VisualizaTabla(tabla)
        if RellenaUnaCasillaCon2Posibles(tabla):
            print "rellenada 2 posibles"
            # VisualizaTabla(tabla)
        elif RellenaUnaCasillaCon3Posibles(tabla):
            print "rellenada 3 posibles"
            # VisualizaTabla(tabla)
        elif RellenaUnaCasillaCon4Posibles(tabla):
            print "rellenada 4 posibles"
            # VisualizaTabla(tabla)
        elif RellenaUnaCasillaCon5Posibles(tabla):
            print "rellenada 5 posibles"
            # VisualizaTabla(tabla)
        elif RellenaUnaCasillaCon6Posibles(tabla):
            print "rellenada 6 posibles"
            # VisualizaTabla(tabla)
        elif RellenaUnaCasillaCon7Posibles(tabla):
            print "rellenada 7 posibles"
            # VisualizaTabla(tabla)


def OcultaCeldas(tabla, nivel):
    if nivel == "facil":
        maxceros = 35
    elif nivel == "medio":
        maxceros = 39
    else:
        maxceros = 42
    cerosinsertados = 0
    contador = 0
    filas = len(tabla)
    columnas = len(tabla[0])
    while (maxceros > cerosinsertados and contador < 1000):
        contador += 1
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tabla[fila][columna] != 0:
            if len(RetornaTotalPosibles(tabla, fila, columna)) == 1:
                tabla[fila][columna] = 0
                cerosinsertados += 1
                # VisualizaTabla(tabla)


def SolucionaSudoku(tabla):
    ceros = CuentaCeros(tabla)
    bajando = 1
    contador = 0
    print "\nEstado inicial de la tabla"
    VisualizaTabla(tabla)
    print "\nInicialmente hay", ceros, "ceros."
    while ceros > 0 and bajando == 1:
        RellenaInmediatos(tabla)
        if ceros > CuentaCeros(tabla):
            ceros = CuentaCeros(tabla)
            bajando = 1
        else:
            bajando = 0
        contador += 1
        print "En", contador, "pasada quedan", ceros, "ceros"
    print "\nEstado final de la tabla"
    VisualizaTabla(tabla)
    if bajando == 0:
        print "No se pudo solucionar, compruebe que los valores introducidos son correctos"


def Funciones():
    print ""
    print "FUNCIONES CARGADAS:"
    print ""
    print "  CreaTablaBlanco():"
    print "  IntroducirValoresTabla(tabla)"
    print "  VisualizaTabla(tabla)"
    print "  CuentaCeros(tabla)"
    print "  RetornaMinifilas(tabla,cuadrante)"
    print "  RetornaMinicolumnas(tabla,cuadrante)"
    print "  RetornaCuadrante(fila,columna)"
    print "  RetornaPosiblesVertical(tabla,fila,columna)"
    print "  RetornaPosiblesHorizontal(tabla,fila,columna)"
    print "  RetornaPosiblesCuadrante(tabla,fila,columna)"
    print "  RetornaInvertidos(posibles)"
    print "  RetornaTotalPosibles(tabla,fila,columna)"
    print "  CompruebaTerminado(tabla)"
    print "  RellenaInmediatos(tabla)"
    print "  SolucionaSudoku(tabla)"
    print "  RetornaUnoDeLaLista(lista)"
    print "  RellenaCuadrante(tabla,cuadrante)"
    print "  RellenaUnaCasillaCon2Posibles(tabla)"
    print "  RellenaUnaCasillaCon3Posibles(tabla)"
    print "  RellenaUnaCasillaCon4Posibles(tabla)"
    print "  RellenaUnaCasillaCon5Posibles(tabla)"
    print "  RellenaUnaCasillaCon6Posibles(tabla)"
    print "  RellenaUnaCasillaCon7Posibles(tabla)"
    print "  RellenaPosibilidades(tabla)"
    print "  OcultaCeldas(tabla,\"nivel\")"
    print "  MenuPrincipal()\n"


def MenuPrincipal():
    print "Bienvenido a este aplicacion creada por Luis VH 26/11/2010\n"
    print"Desea solucionar un Sudoku? (S/N):"
    deseo = raw_input()
    if deseo.lower() == 's':
        sudoku = CreaTablaBlanco()
        IntroducirValoresTabla(sudoku)
        SolucionaSudoku(sudoku)
    print"Desea generar un Sudoku? (S/N):"
    deseo = raw_input(">>")
    if deseo.lower() == 's':
        print"Nivel de dificultat? (facil=0/medio=1/dificil=2):"
        dificultad = raw_input()
        sudoku = CreaTablaBlanco()
        RellenaCuadrante(sudoku, 1)
        RellenaCuadrante(sudoku, 5)
        RellenaCuadrante(sudoku, 9)
        RellenaPosibilidades(sudoku)
        if dificultad == "0":
            OcultaCeldas(sudoku, "facil")
        elif dificultad == "1":
            OcultaCeldas(sudoku, "medio")
        else:
            OcultaCeldas(sudoku, "dificil")
        VisualizaTabla(sudoku)
        print"Desea ver la solucion ahora? (S/N):"
        solucion = raw_input()
        if solucion.lower() == 's':
            SolucionaSudoku(sudoku)

    print"Recuerde que se han cargado las funciones"
    print"y que puede utilizarlas a su antojo\n"
    print"Realizado por:   Luis VH el 7/12/2010"
    print"Gracias por visitar www.pythonenubuntu.blogspot.com"
    print"Teclee MenuPrincipal() paga solucionar Sudokus"
    print"Teclee Funciones() paga lista de funciones usadas"


# sudoku = CreaTablaBlanco()
# RellenaCuadrante(sudoku,1)
# RellenaCuadrante(sudoku,5)
# RellenaCuadrante(sudoku,9)
# RellenaPosibilidades(sudoku)
# OcultaCeldas(sudoku,"facil")
# SolucionaSudoku(sudoku)
MenuPrincipal()