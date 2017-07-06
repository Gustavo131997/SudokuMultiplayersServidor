import socket
import threading
from Sudoku.Sudoku2 import *

# Clase que hereda de la clase Thread para poder manejar un hilo para
# controlar la lectura y escritura sobre el socket.
class Socket(threading.Thread):
    def __init__(self, sc, socket_conexion, datos_cliente):
        # informacion de la conexion con el cliente
        self.datos_cliente = datos_cliente
        # socket que recibe para manejar
        self.sc = sc
        self.socket_conexion = socket_conexion
        # inicializar el constructor del hilo
        threading.Thread.__init__(self)
        self.stoprequest = threading.Event()
        # variable para definir cuando detener el hilo
        self.condicion = True

    def leer(self):
        try:
            bufSize = 1024
            datos_recibidos = self.sc.recv(bufSize)
            return datos_recibidos.decode('utf-8')
        except socket.error as msg:
            print("Socket Error: %s" % msg)

    def escribir(self, mensaje):
        # enviar mensaje en formato utf8
        self.sc.send(mensaje.encode('utf8'))

    def desconectar(self):
        # terminar socket
        self.sc.close()

    # imprime la informacion de conexion con el cliente
    def imprimir(self):
        print(self.datos_cliente)

    def run(self):
        while self.condicion:
            # controla si se produce un erro on el escritura
            try:

                trama = self.leer()
                # print("trama->"+trama);
                # cuando la conexion rebiba la palabra exit termina
                if trama == "EXIT" or trama is None:
                    # desconecta y elimina el socket de la lista
                    self.socket_conexion.eliminar_socket(self)
                    self.desconectar()
                    self.condicion = False
                    print('cliente desconectado')
                else:
                    # print(trama)
                    self.escribir("Phyton dice recibido '" + trama + "'");

            except socket.error as msg:
                self.socket_conexion.eliminar_socket(self)
                self.desconectar()

    def run2(self):
        while self.condicion:
            # controla si se produce un erro on el escritura
            try:

                trama = self.leer()
                # print("trama->"+trama);
                # cuando la conexion rebiba la palabra exit termina
                if trama == "EXIT" or trama is None:
                    # desconecta y elimina el socket de la lista
                    self.socket_conexion.eliminar_socket(self)
                    self.desconectar()
                    self.condicion = False
                    print('cliente desconectado')
                else:
                    if trama == "1":
                        sudoku1 = Sudoku()
                        self.escribir("Nivel de dificultat? (facil=0/medio=1/dificil=2):")
                        dificultad = self.leer()
                        sudoku1.RellenaCuadrante(1)
                        sudoku1.RellenaCuadrante(5)
                        sudoku1.RellenaCuadrante(9)
                        sudoku1.RellenaPosibilidades()
                        if dificultad == "0":
                            sudoku1.OcultaCeldas("facil")
                        elif dificultad == "1":
                            sudoku1.OcultaCeldas("medio")
                        else:
                            sudoku1.OcultaCeldas("dificil")
                        sudoku.VisualizaTabla()
                        self.escribir("tablero_0")
                        self.escribir("linea_1")
                        for i in range(0,10):
                            self.escribir(sudoku1.tablero[0][1])

                        sudoku2 = Sudoku()

                    self.escribir("tablero_0")
                    for i in range(0, 3):
                        for j in range(0, 3):
                            for k in range(0, 3):
                                for z in range(0, 3):
                                    self.escribir("macrofila:" + str(i) + "macrocolumna:" + str(j) + "fila:" + str(k) + "columna:" + str(z) + "valor:" + sudoku1.tablero[i][j][k][z][0])
                    # print(trama)
                    self.escribir("Phyton dice recibido '" + trama + "'");

            except socket.error as msg:
                self.socket_conexion.eliminar_socket(self)
                self.desconectar()





