import socket
import re
import os

class FTPClient:
    def init(self, host, port=21):
        self.host = host
        self.port = port
        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.control_socket.settimeout(10)

    def connect(self,username='anonymous', password=''):
        self.control_socket.connect((self.host, self.port))
        self.userName = username
        self.password = password
        return self.getResponse()

    def getResponse(self):
        response = ''
        while True:
            part = self.control_socket.recv(1024).decode()
            response += part
            if response.endswith('\r\n') or len(part) < 1024:
                break
        return response

    def SendCommand(self, command):
        self.control_socket.sendall(f"{command}\r\n".encode())
        return self.getResponse()

    def logIn(self):
        self.SendCommand(f'USER {self.userName}')
        return self.SendCommand(f'PASS {self.password}')

    def passiveMode(self):
        resp = self.SendCommand('PASV')
        ipPortPattern = re.compile(r'(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)')
        ipPortMatch = ipPortPattern.search(resp)
        if ipPortMatch:
            ip_address = '.'.join(ipPortMatch.groups()[:4])
            port = (int(ipPortMatch.group(5)) << 8) + \
                int(ipPortMatch.group(6))
            DataTransmissionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            DataTransmissionSocket.connect((ip_address, port))
            return DataTransmissionSocket
        else:
            print("Could not stable a data connection.")
            return None

    def list(self, directory=""):
        try:
            DataTransmissionSocket = self.passiveMode()
            if DataTransmissionSocket is None:
                print("Could not stable a data connection.")
                return
            self.SendCommand(f'LIST {directory}')
            resp = ""
            while True:
                part = DataTransmissionSocket.recv(4096).decode()
                if not part:
                    break
                resp += part
            print(resp)
            DataTransmissionSocket.close()
            return resp
    
        except Exception as e:
            print(f"Error al listar archivos: {e}")

    def print_working_directory(self):
        return self.SendCommand('PWD')
    
    def mkdir(self, nombre: str):
        """
        Crea un directorio en el servidor FTP.

        Args:
            nombre (str): El nombre del directorio a crear.
        """
        self.SendCommand('MKD ' + nombre)

    def rmdir(self, nombre: str):
        """
        Elimina un directorio en el servidor FTP.

        Args:
            nombre (str): El nombre del directorio a eliminar.
        """
        self.SendCommand('RMD ' + nombre)

    def get_size(self, nombre: str):
        """
        Obtiene el tamaño de un archivo en el servidor FTP.

        Args:
            nombre (str): El nombre del archivo del que se quiere obtener el tamaño.
        """
        self.SendCommand('SIZE ' + nombre)
    def Download(self, remoteDirectory: str, type='A'):
        data_socket = self.passiveMode()
        if not data_socket:
            return "Error estableciendo modo PASV."
        self.SendCommand(f'TYPE {type}')
        self.SendCommand(f'RETR {remoteDirectory}')
        #self.read_response()
        with open(remoteDirectory.split('/')[-1], 'wb') as file:
            while True:
                data = data_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        data_socket.close()
        return self.getResponse()

    def UpLoad(self, local_filename, filename):
        """Sube un archivo al servidor FTP."""
        file_path = os.path.abspath(os.path.join(os.getcwd(), local_filename))
        
        if not os.path.exists(file_path):
            return f"Error, file '{file_path}' not found"
        
        data_socket = self.passiveMode()
        if not data_socket:
            return "Error estableciendo modo PASV."
        
        resp = self.SendCommand(f'STOR {filename}')

        if(resp[0]!='5'): 
            with open(local_filename, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    data_socket.sendall(data)
            data_socket.close()
            return self.getResponse()
        else:
            print("Permisos insuficientes")
            data_socket.close()
            return resp  
        
    def exit(self):
        response = self.SendCommand('QUIT')
        self.control_socket.close()
        return response