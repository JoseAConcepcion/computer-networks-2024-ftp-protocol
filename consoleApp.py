from Redes import FTPClient
import time
def Application():
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
    while True:
        print('Por favor introduzca el comando: ')
        commandParts = input().strip().split(" ")
        command = commandParts[0].lower()
        params = commandParts[1:]
        
        
        if command == 'terminate':
            print('Desconectando.')
            print('Desconectando..')
            print('Desconectando...')
            break
        if command == 'cd':
            print(cliente.cwd(*params))
            continue
        if command == 'mkdir':
            print(cliente.mkdir(*params))
            continue
        if command == 'rmdir':
            print(cliente.rmdir(*params))
            continue
        if command == 'ls':
            print(cliente.nlist(*params))
            print(cliente.getResponse())
            continue
        if command == 'ls-a':
            print(cliente.list(*params))
            print(cliente.getResponse())
            continue
        if command == 'exit':
            print(cliente.exit())
            continue
        if command == 'pwd':
            print(cliente.print_working_directory())
            continue
        if command == 'upload':
            print(cliente.UpLoad(*params))
            continue
        if command == 'download':
            print(cliente.Download(*params))
            continue
        if command == 'continueive':
            print(cliente.continueiveMode())
            continue
        if command == 'sizeof':
            print(cliente.get_size(*params))
            continue
        if command == 'help':
            print(cliente.help(*params))
            continue
        if command == 'cancel':
            print(cliente.abor())
            continue
        if command == 'noop':
            print(cliente.NoOp())
            continue
        if command == 'rename':
            print(cliente.rename(*params))
            continue
        if command == 'status':
            print(cliente.getStatus(*params))
            continue
        if command == 'system':
            print(cliente.getSystem())
            continue
        if command == 'siteparams':
            print(cliente.getSiteParameters())
            continue
        if command == 'delete':
            print(cliente.deleteFile(*params))
            continue
        if command == 'restarttransfer':
            print(cliente.restartTransfer(*params))
            continue
        if command == 'cdup':
            print(cliente.CDUP())
            continue
        if command == 'port':
            print(cliente.DataPort(*params))
            continue
        if command == 'acc':
            print(cliente.Account(*params))
            continue
        if command == 'reinitialize':
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
        if command == 'uploadu':
            print(cliente.UploadUnique(*params))
            continue
        if command == 'append':
            print(cliente.Append(*params))
            continue
        if command == 'allocate':
            print(cliente.Allocate(*params))
            continue
