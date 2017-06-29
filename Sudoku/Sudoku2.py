# -*- coding: cp1252 -*-
import random


class Sudoku():
    """docstring for Sudoku"""
    def __init__(self):
        self.tablero = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def RellenaCuadrante(self, cuadrante=1):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        minifilas = self.RetornaMinifilas(cuadrante)
        minicolumnas = self.RetornaMinicolumnas(cuadrante)
        for i in minifilas:
            for j in minicolumnas:
                longitud = len(disponibles)
                aleatorio = random.randint(0, longitud - 1)
                self.tablero[i][j] = disponibles[aleatorio]
                disponibles.remove(disponibles[aleatorio])


    def CreaTablaBlanco(self):
        return [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    def IntroducirValoresTabla(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        print "Vamos a introducir los valores del sudoku para llenar la self.tablero"
        print "Indtroduzca los valores de izquierda a derecha y de arriba a bajo"
        print "En las casillas sin valor introduzca un 0"
        filasentrada = [[], [], [], [], [], [], [], [], []]
        for i in range(9):
            while len(filasentrada[i]) != 9:
                print"Introduzca los valores de la fila", i + 1,
                filasentrada[i] = raw_input()
        for i in range(filas):
            for j in range(columnas):
                self.tablero[i][j] = int(filasentrada[i][j])


    def VisualizaTabla(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            if i == 0 or i == 3 or i == 6: print "- - - - - - - - - - - - -"
            for j in range(columnas):
                if j == 0 or j == 3 or j == 6: print "|",
                print self.tablero[i][j]
                if j == 8: print"|"
            if i == 8: print "- - - - - - - - - - - - -"
        # print "\n"


    def CuentaCeros(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        ceros = 0
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:
                    ceros += 1
        return ceros


    def RetornaMinifilas(self, cuadrante):
        if cuadrante == 1 or cuadrante == 2 or cuadrante == 3:
            return [0, 1, 2]
        elif cuadrante == 4 or cuadrante == 5 or cuadrante == 6:
            return [3, 4, 5]
        elif cuadrante == 7 or cuadrante == 8 or cuadrante == 9:
            return [6, 7, 8]


    def RetornaMinicolumnas(self, cuadrante):
        if cuadrante == 1 or cuadrante == 4 or cuadrante == 7:
            return [0, 1, 2]
        elif cuadrante == 2 or cuadrante == 5 or cuadrante == 8:
            return [3, 4, 5]
        elif cuadrante == 3 or cuadrante == 6 or cuadrante == 9:
            return [6, 7, 8]


    def RetornaCuadrante(self, fila, columna):
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


    def RetornaPosiblesVertical(self, fila, columna):
        disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        filas = len(self.tablero)
        for i in range(filas):
            if i != fila:
                valor = self.tablero[i][columna]  # valor que hay asignado
                if valor in disponibles:  # si el valor que hemos leido esta en la lista
                    disponibles.remove(valor)  # lo borramos de la lista ya que no disponible
        return disponibles


    def RetornaPosiblesHorizontal(self, fila, columna):
        disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        columnas = len(self.tablero[0])
        for i in range(columnas):
            if i != columna:
                valor = self.tablero[fila][i]  # valor que hay asignado
                if valor in disponibles:  # si el valor que hemos leido esta en la lista
                    disponibles.remove(valor)  # lo borramos de la lista ya que no disponible
        return disponibles


    def RetornaPosiblesCuadrante(self, fila, columna):
        disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cuadrante = self.RetornaCuadrante(fila, columna)
        minifilas = self.RetornaMinifilas(cuadrante)
        minicolumnas = self.RetornaMinicolumnas(cuadrante)
        valorinicialenpuntoestudio = self.tablero[fila][columna]
        self.tablero[fila][columna] = 'estudio'
        for i in minifilas:
            for j in minicolumnas:
                if self.tablero[i][j] != 'estudio':
                    valor = self.tablero[i][j]
                    if valor in disponibles:
                        disponibles.remove(valor)
        self.tablero[fila][columna] = valorinicialenpuntoestudio  # volvemos a poner el valor inicial
        return disponibles


    def RetornaInvertidos(self, posibles):
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


    def RetornaTotalPosibles(self, fila, columna):
        lista1 = self.RetornaPosiblesVertical(fila, columna)
        lista2 = self.RetornaPosiblesHorizontal(fila, columna)
        lista3 = self.RetornaPosiblesCuadrante(fila, columna)
        lista1 = self.RetornaInvertidos(lista1)
        lista2 = self.RetornaInvertidos(lista2)
        lista3 = self.RetornaInvertidos(lista3)
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
        listaposibles = self.RetornaInvertidos(listaimposibles)
        return listaposibles


    def CompruebaTerminado(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            valor = 0
            for j in range(columnas):
                valor += self.tablero[i][j]
            print "La suma de columna=", i, "es de", valor
        for j in range(columnas):
            valor = 0
            for i in range(filas):
                valor += self.tablero[i][j]
            print "La suma de fila=", i, "es de", valor


    def RellenaInmediatos(self):
        actuado = 0
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 1:
                        self.tablero[i][j] = posibles[0]
                        actuado = 1
        return actuado


    def RetornaUnoDeLaLista(self, lista):
        longitud = len(lista)
        return lista[random.randint(0, longitud - 1)]


    def RellenaUnaCasillaCon2Posibles(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:  # casilla vacia
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 2:
                        self.tablero[i][j] = self.RetornaUnoDeLaLista(posibles)
                        return 1
        return 0


    def RellenaUnaCasillaCon3Posibles(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:  # casilla vacia
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 3:
                        self.tablero[i][j] = self.RetornaUnoDeLaLista(posibles)
                        return 1
        return 0


    def RellenaUnaCasillaCon4Posibles(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:  # casilla vacia
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 4:
                        self.tablero[i][j] = self.RetornaUnoDeLaLista(posibles)
                        return 1
        return 0


    def RellenaUnaCasillaCon5Posibles(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:  # casilla vacia
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 5:
                        self.tablero[i][j] = self.RetornaUnoDeLaLista(posibles)
                        return 1
        return 0


    def RellenaUnaCasillaCon6Posibles(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:  # casilla vacia
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 6:
                        self.tablero[i][j] = self.RetornaUnoDeLaLista(posibles)
                        return 1
        return 0


    def RellenaUnaCasillaCon7Posibles(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        for i in range(filas):
            for j in range(columnas):
                if self.tablero[i][j] == 0:  # casilla vacia
                    posibles = self.RetornaTotalPosibles(i, j)
                    if len(posibles) == 7:
                        self.tablero[i][j] = self.RetornaUnoDeLaLista(posibles)
                        return 1
        return 0


    def RellenaPosibilidades(self):
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        contador = 0
        while self.CuentaCeros() != 0 and contador <= 200:
            contador += 1
            while self.RellenaInmediatos() == 1:
                print "rellenada inmediatos"
                # VisualizaTabla(self.tablero)
            if self.RellenaUnaCasillaCon2Posibles():
                print "rellenada 2 posibles"
                # VisualizaTabla(self.tablero)
            elif self.RellenaUnaCasillaCon3Posibles():
                print "rellenada 3 posibles"
                # VisualizaTabla(self.tablero)
            elif self.RellenaUnaCasillaCon4Posibles():
                print "rellenada 4 posibles"
                # VisualizaTabla(self.tablero)
            elif self.RellenaUnaCasillaCon5Posibles():
                print "rellenada 5 posibles"
                # VisualizaTabla(self.tablero).
            elif self.RellenaUnaCasillaCon6Posibles():
                print "rellenada 6 posibles"
                # VisualizaTabla(self.tablero)
            elif self.RellenaUnaCasillaCon7Posibles():
                print "rellenada 7 posibles"
                # VisualizaTabla(self.tablero)


    def OcultaCeldas(self, nivel):
        if nivel == "facil":
            maxceros = 35
        elif nivel == "medio":
            maxceros = 39
        else:
            maxceros = 42
        cerosinsertados = 0
        contador = 0
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        while (maxceros > cerosinsertados and contador < 1000):
            contador += 1
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            if self.tablero[fila][columna] != 0:
                if len(self.RetornaTotalPosibles(fila, columna)) == 1:
                    self.tablero[fila][columna] = 0
                    cerosinsertados += 1
                    # VisualizaTabla(self.tablero)


    def SolucionaSudoku(self):
        ceros = self.CuentaCeros()
        bajando = 1
        contador = 0
        print "\nEstado inicial de la tablero"
        self.VisualizaTabla()
        print "\nInicialmente hay", ceros, "ceros."
        while ceros > 0 and bajando == 1:
            self.RellenaInmediatos()
            if ceros > self.CuentaCeros():
                ceros = self.CuentaCeros()
                bajando = 1
            else:
                bajando = 0
            contador += 1
            print "En", contador, "pasada quedan", ceros, "ceros"
        print "\nEstado final de la tablero"
        self.VisualizaTabla()
        if bajando == 0:
            print "No se pudo solucionar, compruebe que los valores introducidos son correctos"


    def Funciones(self):
        print ""
        print "FUNCIONES CARGADAS:"
        print ""
        print "  CreaTablaBlanco():"
        print "  IntroducirValoresTabla(tablero)"
        print "  VisualizaTabla(tablero)"
        print "  CuentaCeros()"
        print "  RetornaMinifilas(cuadrante)"
        print "  RetornaMinicolumnas(cuadrante)"
        print "  RetornaCuadrante(fila,columna)"
        print "  RetornaPosiblesVertical(fila,columna)"
        print "  RetornaPosiblesHorizontal(fila,columna)"
        print "  RetornaPosiblesCuadrante(fila,columna)"
        print "  RetornaInvertidos(posibles)"
        print "  RetornaTotalPosibles(fila,columna)"
        print "  CompruebaTerminado()"
        print "  RellenaInmediatos()"
        print "  SolucionaSudoku()"
        print "  RetornaUnoDeLaLista(lista)"
        print "  RellenaCuadrante(cuadrante)"
        print "  RellenaUnaCasillaCon2Posibles()"
        print "  RellenaUnaCasillaCon3Posibles()"
        print "  RellenaUnaCasillaCon4Posibles()"
        print "  RellenaUnaCasillaCon5Posibles()"
        print "  RellenaUnaCasillaCon6Posibles()"
        print "  RellenaUnaCasillaCon7Posibles()"
        print "  RellenaPosibilidades()"
        print "  OcultaCeldas(\"nivel\")"
        print "  MenuPrincipal()\n"


    def MenuPrincipal(self):
        print "Bienvenido a este aplicacion creada por Luis VH 26/11/2010\n"
        print"Desea solucionar un Sudoku? (S/N):"
        deseo = raw_input()
        if deseo.lower() == 's':
            sudoku = Sudoku()
            sudoku.IntroducirValoresTabla()
            sudoku.SolucionaSudoku()
        print"Desea generar un Sudoku? (S/N):"
        deseo = raw_input(">>")
        if deseo.lower() == 's':
            print"Nivel de dificultat? (facil=0/medio=1/dificil=2):"
            dificultad = raw_input()
            sudoku = Sudoku()
            sudoku.RellenaCuadrante(1)
            sudoku.RellenaCuadrante(5)
            sudoku.RellenaCuadrante(9)
            sudoku.RellenaPosibilidades()
            if dificultad == "0":
                sudoku.OcultaCeldas("facil")
            elif dificultad == "1":
                sudoku.OcultaCeldas("medio")
            else:
                sudoku.OcultaCeldas("dificil")
            sudoku.VisualizaTabla()
            print"Desea ver la solucion ahora? (S/N):"
            solucion = raw_input()
            if solucion.lower() == 's':
                sudoku.SolucionaSudoku()

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
if __name__ == "__main__":
    sudoku = Sudoku();
    sudoku.MenuPrincipal()