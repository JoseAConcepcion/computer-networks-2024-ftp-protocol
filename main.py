from Redes import FTPClient
import time
import consoleApp

def main():
    # while True:
    #     print("Introduzca el IP del servidor al cual realizar la conexión")

        #preguntar por el puerto sino 21 default
        #realizar la conexion y esperar por comandos
    

    # cliente = ClienteFTP('eu-central-1.sftpcloud.io', 21) #test.rebex.net para probar con un servidor FTP
    # cliente.conectar('2e6ff3ba070c418982b0dbbbf2b55ebe', "8Xvdb8ABDg8Z2rk2ThpB2yCiBrUFEdt9")


    cliente = FTPClient('194.108.117.16')  
    print(cliente.connect())
    print(cliente.logIn())
    # print(cliente.getStatus('/pub'))
    # todo probar el delete file
    print(cliente.nlist())
    print(cliente.SendCommand('PWD'))
    print(cliente.list())
    # time.sleep(10)

    # print(cliente.cwd('/pub'))
    # print(cliente.SendCommand('PWD'))
    
    # print(cliente.list('/pub'))
    print(cliente.exit())

if __name__ == "__main__":
    # main()
    consoleApp.Application()