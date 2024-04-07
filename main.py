from Redes import * 
import time

def main():
    # while True:
    #     print("Introduzca el IP del servidor al cual realizar la conexión")

        #preguntar por el puerto sino 21 default
        #realizar la conexion y esperar por comandos
    cliente = ClienteFTP('eu-central-1.sftpcloud.io', 21) #test.rebex.net para probar con un servidor FTP
    # 194.108.117.16
    cliente.conectar('2e6ff3ba070c418982b0dbbbf2b55ebe', "8Xvdb8ABDg8Z2rk2ThpB2yCiBrUFEdt9")
    # cliente.enviar_comando('USER')
    # cliente.enviar_comando('PASS')
    cliente.enviar_comando('PWD')
    # cliente.mkdir("new")
    cliente.rmdir('new')
    cliente.enviar_comando('CWD new')
    # cliente.enviar_comando('HELP SITE')
    # cliente.enviar_comando('SIZE readme.txt')
    # cliente.enviar_comando('CWD pub')
    cliente.enviar_comando('PWD')
    cliente.enviar_comando('CWD example')
    cliente.enviar_comando('PWD')
    cliente.probar_listar()
    # cliente.mkdir('test')
    cliente.enviar_comando('PWD')
    # cliente.probar_listar()
    #! estos dos no funcionan porque esperan info adicional
    #! Rejecting data connection. Send 'EPSV', 'EPRT', 'PASV' or 'PORT' first.
    # cliente.enviar_comando('PASV')
    # cliente.enviar_comando('LIST')
    # cliente.enviar_comando('TYPE A')
    # cliente.enviar_comando('PASV')
    # cliente.enviar_comando('NLST') 
    # cliente.probar_listar()

    # cliente.enviar_comando('CDUP')
    cliente.desconectar()
    

if __name__ == "__main__":
    main()