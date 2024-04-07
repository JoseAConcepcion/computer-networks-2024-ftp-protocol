from Redes import * 
import time

def main():
    # while True:
    #     print("Introduzca el IP del servidor al cual realizar la conexión")

        #preguntar por el puerto sino 21 default
        #realizar la conexion y esperar por comandos
    cliente = ClienteFTP('194.108.117.16', 21) #test.rebex.net para probar con un servidor FTP
    cliente.conectar()
    cliente.enviar_comando('USER anonymous')
    cliente.enviar_comando('PASS')
    cliente.enviar_comando('PWD')
    cliente.enviar_comando('HELP SITE')
    cliente.enviar_comando('CWD pub')
    cliente.enviar_comando('PWD')
    #! estos dos no funcionan porque esperan info adicional
    #! Rejecting data connection. Send 'EPSV', 'EPRT', 'PASV' or 'PORT' first.
    cliente.enviar_comando('PASV')
    cliente.enviar_comando('LIST')
    cliente.enviar_comando('TYPE A')
    # cliente.enviar_comando('PASV')
    # cliente.enviar_comando('NLST') 
    cliente.probar_listar()

    # cliente.enviar_comando('CDUP')
    cliente.desconectar()
    

if __name__ == "__main__":
    main()