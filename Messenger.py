import socket

def mp():
    choose = input('select an action (send/receive): ')

    if choose == 'receive':
        port = input('Enter port: ')
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind(('',int(port)))
        soc.listen(1)

        print('waiting connection...')

        while True:
            con, addr = soc.accept()
            print("Connected clinet :" , con)
            try:
                filename = con.recv(1024)
                with open(filename,'wb') as file:
                    while True:
                        recvfile = con.recv(1024)
                        if recvfile: 
                            file.write(recvfile)
                            break
            except IOError:
                m = filename.decode()
                print(m)
                break
        print('File or text has been received.')
         
    elif choose == 'send': 
    
        filename = input('enter file name (with extension) or text: ')

        address = input('Enter IP-address (X.X.X.X): ')
        port = input('Enter port: ')

        soc = socket.socket()
        soc.connect((str(address),int(port)))
        
        try:
            f = open(filename)
            with open(filename, 'rb') as file:
                soc.sendall(bytes(filename, 'UTF-8'))
                sendfile = file.read()
                soc.sendall(sendfile)
            print('file sent')
        except IOError:
            soc.sendall(bytes(filename,'UTF-8'))

    else:
        print("Houston, we're in trouble...")

mp()
while True:
    cont = input('Continue (y/n)? ')
    if cont == 'y':
        mp()
    if cont == 'n':
        print('Bye')
