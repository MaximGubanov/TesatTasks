import socket


def client():

    sock = socket.socket()
    sock.connect(('localhost', 7777))

    while True:
        message = input('-> ')
        if message == 'exit':
            break
        sock.send(message.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        print(f'Сообщение от сервера: -> {data}')

    sock.close()


if __name__ == '__main__':
    client()
