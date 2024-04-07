import socket
import re
import os

class FTPClient:

    def __init__(self, host, port=21):
        self.host = host
        self.port = port
        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.control_socket.settimeout(10)

    def connect(self, username='anonymous', password=''):
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
            # print(resp)
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
        
    def abor(self):
        return self.SendCommand('ABOR')
        
    def cwd(self, path):
        return self.SendCommand('CWD ' + path)
    
    def help(self, args=""):
        return self.SendCommand('HELP ' + args)
    
    def NoOp(self):
        return self.SendCommand('NOOP')
    def rename(self, oldName, newName):
        resp = self.SendCommand('RNFR ' + oldName)
        if resp[0] != '3':
            print('error al renombrar, no existe el archivo')
            return
        return self.SendCommand('RNTO ' + newName) 
    
    # este comando puede estar implementado o no en el servidor
    def getStatus(self, path=None):
        if path is None:
            return self.SendCommand('STAT')
        else:
            return self.SendCommand('STAT ' + path)
    
    def getSystem(self):
        return self.SendCommand('SYST')
    
    def getSiteParameters(self):
        return self.SendCommand('SITE')
    
    def nlist(self, path=''):
        try:
            DataTransmissionSocket = self.passiveMode()
            if DataTransmissionSocket is None:
                print("No se pudo conectar al socket")
                return
            self.SendCommand(f'NLST ' + path)
            resp = ""
            while True:
                part = DataTransmissionSocket.recv(4096).decode()
                if not part:
                    break
                resp += part
            DataTransmissionSocket.close()
            return resp

        except Exception as e:
            print(f"Error al listar archivos: {e}")
            
    def deleteFile(self, path):
        return self.SendCommand('DELE ' + path)
    
    def restartTransfer(self, marker):
        return self.SendCommand('REST ' + marker)
    
    def CDUP(self):
        return self.SendCommand('CDUP')
    def DataPort(self, ip, port):
        return self.SendCommand(f'PORT {ip},{port}')

    def Account(self, account):
        return self.SendCommand('ACCT ' + account)
    def Reinitialize(self):
        return self.SendCommand('REIN')
    def FileStructure(self, structure):
        if(structure in ('F', 'R', 'P')):
            return self.SendCommand('STRU ' + structure)
        else:
            return "Error, 'structure' must be 'F', 'R', or 'P'."
    def StructureMount(self, structure):        
        return self.SendCommand('SMNT ' + structure)
    def TransferMode(self, mode):
        if(mode in ('S', 'B', 'C')):
            return self.SendCommand('MODE ' + mode)
        else:
            return "Error, 'mode' must be 'S' or 'B' or 'C'."
    def UploadUnique(self, local_filename, filename):
        data_socket = self.passiveMode()
        if not data_socket:
            return "Error estableciendo modo PASV."
        
        resp = self.SendCommand(f'STOU {filename}')

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
    def Append(self, local_filename, filename):
        data_socket = self.passiveMode()
        if not data_socket:
            return "Error estableciendo modo PASV."
        
        resp = self.SendCommand(f'APPE {filename}')

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
    
    def Allocate(self, numberOfBytes, Size = 0):
        if(Size == 0):
            return self.SendCommand('ALLO ' + numberOfBytes)
        else:
            return self.SendCommand('ALLO ' + numberOfBytes + ' ' + 'R' + ' ' + Size)
    def exit(self):
        response = self.SendCommand('QUIT')
        self.control_socket.close()
        return response