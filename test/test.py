from servidor.SocketConexion import *
import sys

if __name__=='__main__':
    socketConexion = SocketConexion('localhost', 9999)
    condicion = True
    while (condicion):
        print("                                                        ")
        print("---------------------------MENU------------------------")
        print("1.- Iniciar Servidor")
        print("2.- Mostrar Todos los clientes")
        print("3.- Parar Servidor")
        print("4.- Salir")
        print("-------->Seleccione una opcion:")

        valor = input(">>")
        valor = int(valor)
        print("                                                        ")
        if valor == 1:
            socketConexion.start()
            print("Servidor Iniciando...")
        elif valor == 2:
            socketConexion.imprimir()
        elif valor == 3:
            socketConexion.detener()
            print("Servidor Detenido")
        elif valor == 4:
            print("Ejecucion terminada")
            sys.exit()