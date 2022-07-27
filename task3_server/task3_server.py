from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import threading


class Server(object):
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.address, self.port))

    def run(self):
        print("[SERVER IS RUNNING]")
        self.sock.listen(10)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            th = threading.Thread(target=self.accepting_client, args=(client, address))
            th.start()

    def accepting_client(self, client, address):
        while True:
            try:
                data = client.recv(1024).decode('utf-8')
                print(f'Получено сообщение от {address} -> {data}')
                if data:
                    client.send(data.upper().encode('utf-8'))
                else:
                    raise ConnectionError('Клиент отсоединился')
            except ConnectionError:
                client.close()
                return False


if __name__ == "__main__":
    server = Server('', 7777)
    server.run()

