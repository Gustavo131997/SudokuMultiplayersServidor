import random

class Sudoku :
    def __init__(self):
        self.tablero = [
            [  # macrocol
                [  # fila
                    [  # una columna
                        list(range(0, 1))  # una celda
                        for c in range(3)
                    ]
                    for f in range(3)
                ]
                for mc in range(3)
            ]
            for nc in range(3)
        ]


    def crearTableroSudoku(self):
        cont = 0
        while cont <= 80 :
            v = random.randrange(1,10)
            mc = random.randrange(0,3)
            mf = random.randrange(0,3)
            f = random.randrange(0,3)
            c = random.randrange(0,3)
            if self.tablero[mf][mc][f][c] == [0]:
                if self.validarIngreso(mf,mc,c,f,v):
                    cont = cont + 1
                    print("-------------------------",cont," ---",v)
                    self.tablero[mf][mc][c][f] = [v]


    def validarColumna(self, mf, f, v):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.tablero[mf][i][f][j] == [v]:
                    print("2.5")
                    return False
        print("2.7")
        return True

    def validarFila(self, mc, c, v):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.tablero[i][mc][j][c] == [v]:
                    print("4.5")
                    return False
        print("4.7")
        return True

    def validarRegion(self, mc, mf, v):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.tablero[mc][mf][i][j] == [v]:
                    print("6.5")
                    return False
        print("6.7")
        return True
    def validarIngreso(self, mf , mc , c , f , v):
        if self.validarRegion(mc,mf,v):
            if self.validarColumna(mf,f,v):
                if self.validarFila(mc,c,v):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

if __name__=='__main__':
    sudoku = Sudoku()
    sudoku.crearTableroSudoku()
    print(sudoku.tablero)
