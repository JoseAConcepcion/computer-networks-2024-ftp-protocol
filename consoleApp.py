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
    cliente = FTPClient(ip, port)
    cliente.connect(user, password)
    cliente.logIn()
    while True:
        print('Por favor introduzca el comando: ')
        command = input()
        if command.lower().split(' ')[0] == 'cd':
            pass
        if command.lower().split(' ')[0] == 'mkdir':
            pass
        if command.lower().split(' ')[0] == 'rmdir':
            pass
        if command.lower().split(' ')[0] == 'ls':
            pass
        if command.lower().split(' ')[0] == 'ls-a':
            pass
        if command.lower().split(' ')[0] == 'exit':
            pass
        if command.lower().split(' ')[0] == 'pwd':
            pass
        if command.lower().split(' ')[0] == 'upload':
            pass
        if command.lower().split(' ')[0] == 'download':
            pass
        if command.lower().split(' ')[0] == 'passive':
            pass
        if command.lower().split(' ')[0] == 'sizeof':
            pass
        if command.lower().split(' ')[0] == 'help':
            pass
        if command.lower().split(' ')[0] == 'cancel':
            pass
        if command.lower().split(' ')[0] == 'noop':
            pass
        if command.lower().split(' ')[0] == 'rename':
            pass
        if command.lower().split(' ')[0] == 'status':
            pass
        if command.lower().split(' ')[0] == 'system':
            pass
        if command.lower().split(' ')[0] == 'siteparams':
            pass
        if command.lower().split(' ')[0] == 'delete':
            pass
        if command.lower().split(' ')[0] == 'restarttransfer':
            pass
        if command.lower().split(' ')[0] == 'cdup':
            pass
        if command.lower().split(' ')[0] == 'port':
            pass
        if command.lower().split(' ')[0] == 'acc':
            pass
        if command.lower().split(' ')[0] == 'reinitialize':
            pass
        if command.lower().split(' ')[0] == 'stru':
            pass
        if command.lower().split(' ')[0] == 'smnt':
            pass
        if command.lower().split(' ')[0] == 'mode':
            pass
        if command.lower().split(' ')[0] == 'uploadu':
            pass
        if command.lower().split(' ')[0] == 'append':
            pass
        if command.lower().split(' ')[0] == 'allocate':
            pass
