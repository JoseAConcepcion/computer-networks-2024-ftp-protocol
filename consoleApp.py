from Redes import FTPClient
def Application():
    print('Por favor introduzca la direccion ip del servidor: ')
    ip = input()
    print('Por favor introduzca el puerto: ')
    port = input()
    print('Por favor introduzca el usuario: ')
    user = input()
    print('Por favor introduzca la contrasena: ')
    password = input()
    if password is None: password = ""
    cliente = FTPClient(ip, int(port))
    if password is '': print('Ejel vacio')
    print(cliente.connect(user, password))
    print(cliente.logIn())
    while True:
        print('Por favor introduzca el comando: ')
        commandParts = input().strip().split(" ")
        command = commandParts[0].lower()
        params = commandParts[1:]
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
            continue
        if command == 'ls-a':
            print(cliente.list(*params))
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
        if command == 'passive':
            print(cliente.passiveMode())
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
        # 
        if command == 'status':
            pass
        if command == 'system':
            pass
        if command == 'siteparams':
            pass
        if command == 'delete':
            pass
        if command == 'restarttransfer':
            pass
        if command == 'cdup':
            pass
        if command == 'port':
            pass
        if command == 'acc':
            pass
        if command == 'reinitialize':
            pass
        if command == 'stru':
            pass
        if command == 'smnt':
            pass
        if command == 'mode':
            pass
        if command == 'uploadu':
            pass
        if command == 'append':
            pass
        if command == 'allocate':
            pass
