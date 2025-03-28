import socket

def server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f'Creando servidor en {host}, puerto {port}')
        s.bind((host, port))
        while True:
            print('Esperando nueva conexión')
            s.listen()
            conn, addr = s.accept()
            print(f'Cliente conectado: {addr}')
            connected = True
            # Keep conection to client open
            while connected:
                data = conn.recv(1024)
                if not data:
                    continue
                data = data.decode('utf-8')
                if data == 'DESCONEXION':
                    print(f'Cerrando conexion con {addr}')
                    connected = False
                    conn.close()
                    continue
                data = data.upper().encode('ascii')
                conn.sendall(data)

if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    try:
        server(host, port)
    except KeyboardInterrupt:
        print('Interrupción de teclado detectada, terminando servidor')
