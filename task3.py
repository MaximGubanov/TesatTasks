from socket import AF_INET, SOCK_STREAM, socket


def server():

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('127.0.0.1', 5000))
    sock.listen(5)

    while True:
        print("Running...")
        client, addr = sock.accept()
        data = client.recv(1024).decode('utf-8')
        print(f"Получено сообщение от: -> {data}")
        headers = 'HTTP/1.1 200 OK\r\n Contetnt-Type: text/html; charset=utf=8\r\n\r\n'.encode('utf-8')
        content = "Response".upper().encode('utf-8')
        client.send(headers + content)


if __name__ == '__main__':
    server()
