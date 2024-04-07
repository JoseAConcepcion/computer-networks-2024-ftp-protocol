"""
Este modulo define la clase `ClienteFTP` que permite conectarse a un servidor FTP y enviar comandos.
"""
import socket

class ClienteFTP:
    """
    Representa un cliente FTP. Permite conectarse a un servidor FTP y enviar comandos.

    Args:
        host (str): El host al que se va a conectar.
        puerto (int): El numero de puerto al que se va a conectar.

    Attributes:
        host (str): El host al que se va a conectar.
        puerto (int): El numero de puerto al que se va a conectar.
        socket (socket.socket): El socket utilizado para la conexion.
    """
    def __init__(self, host: str, puerto: int):
        """
        Inicializa el cliente FTP.

        Args:
            host (str): El host al que se va a conectar.
            puerto (int): El numero de puerto al que se va a conectar.
        """
        self.host = host
        self.puerto = puerto

    def conectar(self, user = '', password = ''):
        """
        Crea un socket y se conecta al servidor FTP.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.puerto))

        # * estableciendo la conexion pasiva por defecto en ipv4
        self.socket.sendall(bytes('PASV' + '\r\n', 'utf-8'))
        if not user:
            user = 'anonymous'
        if not password:
            password = ''
        
        response = self.enviar_comando('USER ' + user)
        response = self.enviar_comando('PASS ' + password)
        return response

    def desconectar(self):
        """
        Desconecta el socket del servidor FTP.
        """
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print("desconectado con exito")

    def enviar_comando(self, comando: str):
        """
        Envia un comando al servidor FTP.

        Args:
            comando (str): El comando a enviar.
        """
        self.socket.sendall(bytes(comando + '\r\n', 'utf-8'))
        respuesta = self.socket.recv(4096).decode('utf-8')
        print(respuesta, end='')

    def mkdir(self, nombre: str):
        """
        Crea un directorio en el servidor FTP.

        Args:
            nombre (str): El nombre del directorio a crear.
        """
        self.enviar_comando('MKD ' + nombre)

    def rmdir(self, nombre: str):
        """
        Elimina un directorio en el servidor FTP.

        Args:
            nombre (str): El nombre del directorio a eliminar.
        """
        self.enviar_comando('RMD ' + nombre)

    # def probar_listar(self):
    #     self.socket.sendall('PASV\r\n'.encode('utf-8'))
    #     mensaje_pasivo = self.socket.recv(4096).decode('utf-8')
        
    #     self.socket.sendall('LIST\r\n'.encode('utf-8'))
    #     # direccion_datos = ('', puerto)
    #     direccion_datos = ('194.108.117.16', 1024)
    #     datos_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

