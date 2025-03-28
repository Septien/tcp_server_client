import socket

def client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'Conectandose a {host}, en el puerto {port}')
        s.connect((host, port))
        send = True
        while send:
            msg = input("Ingresa un mensaje: ")
            print(f'Mensaje a mandar: {msg}')
            s.sendall(msg.encode('ascii'))
            if msg == 'DESCONEXION':
                send = False
                continue
            recvlen = len(msg)
            recv_msg = ''
            while recvlen > 0:
                data = s.recv(1024)
                recvlen -= len(data)
                recv_msg += data.decode('utf-8')
            print(f'Respuesta de servidor: {recv_msg}')

if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    client(host, port)
