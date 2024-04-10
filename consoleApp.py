from Redes import FTPClient
import time
import threading
def Application():
    while True:
        try:
            print('Por favor introduzca la direccion ip del servidor: ')
            ip = input()
            print('Por favor introduzca el puerto: ')
            port = input()
            print('Por favor introduzca el usuario: ')
            user = input()
            print('Por favor introduzca la contrasena: ')
            continueword = input()
            if continueword is None: continueword = ""
            cliente = FTPClient(ip, int(port))
            if continueword is '': print('Ejel vacio')
            print(cliente.connect(user, continueword))
            print(cliente.logIn())
            break
        except Exception as e:
            print("\n etecsa se porta mal \n")
            print(e)
            
    while True:
        print('Por favor introduzca el comando: ')
        commandParts = input().strip().split(" ")
        command = commandParts[0].lower()
        params = commandParts[1:]

        
        if command == 'cwd':
            print(cliente.cwd(*params))
            continue
        if command == 'mkd':
            print(cliente.mkdir(*params))
            continue
        if command == 'rmd':
            print(cliente.rmdir(*params))
            continue
        if command == 'nlst':
            def DownloadUnique():
                print(cliente.nlist(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=DownloadUnique)
            t.start()
            continue
        if command == 'list':
            def Append():
                print(cliente.list(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=Append)
            t.start()
            continue
        if command == 'quit':
            print(cliente.exit())
            break
        if command == 'pwd':
            print(cliente.print_working_directory())
            continue
        if command == 'stor':
            def UpLoad():
                print(cliente.UpLoad(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=UpLoad)
            t.start()
            continue
        if command == 'retr':
            def Download():
                print(cliente.Download(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=Download)
            t.start()
            continue
        if command == 'pass':
            print(cliente.passiveMode())
            continue
        if command == 'size':
            print(cliente.get_size(*params))
            continue
        if command == 'help':
            def help():
                print(cliente.help(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=help)
            t.start()
            continue
        if command == 'abor':
            print(cliente.abor())
            print(cliente.getResponse())
            continue
        if command == 'noop':
            print(cliente.NoOp())
            continue
        if command == 'rename':
            print(cliente.rename(*params))
            continue
        if command == 'stat':
            print(cliente.getStatus(*params))
            continue
        if command == 'syst':
            print(cliente.getSystem())
            continue
        if command == 'site':
            print(cliente.getSiteParameters())
            continue
        if command == 'dele':
            print(cliente.deleteFile(*params))
            continue
        if command == 'rest':
            print(cliente.restartTransfer(*params))
            continue
        if command == 'cdup':
            print(cliente.CDUP())
            continue
        if command == 'port':
            print(cliente.DataPort(*params))
            continue
        if command == 'acct':
            print(cliente.Account(*params))
            continue
        if command == 'rein':
            print(cliente.Reinitialize())
            continue
        if command == 'stru':
            print(cliente.FileStructure())
            continue
        if command == 'smnt':
            print(cliente.StructureMount())
            continue
        if command == 'mode':
            print(cliente.TransferMode())
            continue
        if command == 'stou':
            def UploadUnique():
                print(cliente.UploadUnique(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=UploadUnique)
            t.start()
            continue
        if command == 'appe':
            def Append():
                print(cliente.Append(*params))
                print(cliente.getResponse())
            t = threading.Thread(target=Append)
            t.start()
            continue
        if command == 'allo':
            print(cliente.Allocate(*params))
            continue
        if command == 'user':
            print(cliente.user(*params))
        if command == 'pass':
            print(cliente.password(*params))
        else:
            print("comando no reconocido")
            continue
