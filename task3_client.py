import sys
from socket import AF_INET, SOCK_STREAM, socket


class Client:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)

    def run(self):
        self.sock.connect((self.address, self.port))

        while True:
            message = input('Введите сообщение: ')

            if message == 'quit':
                print("[CLIENT_APP STOPPED ]")
                break

            self.sock.send(message.encode('utf-8'))
            response = self.sock.recv(1024).decode('utf-8')
            print(f"Ответ -> {response}")


if __name__ == '__main__':
    host = sys.argv[1]

    client = Client(host, 7777)
    client.run()
