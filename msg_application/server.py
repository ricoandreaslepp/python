# import uuid; uuid = str(uuid.uuid4()) # for future use

from config import HOST, PORT
import socket
from threading import Thread
from logger import log

# don't know if this should be global
client_connections = []


class Client(Thread):

    def __init__(self, conn, addr, name):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.name = name

    def check_messages(self):
        pass

    def send_message(self):
        pass

    # just for testing
    def recv_message(self):
        self.conn.recv(1024).decode()

    # Thread method
    def run(self):
        self.conn.send("Successfully connected to server...\n".encode())

        # needs an error check
        while True:
            self.conn.send("Do what: ".encode())
            action = self.conn.recv(1024).decode().strip()

            if action == "recv":
                self.recv_message()
                break

            # else send data
            self.conn.send("Send \"who, what\": ".encode())
            # ignore exceptions for now
            data = self.conn.recv(1024).decode().strip()

            # do we care for how the connection was closed?
            if data in ["bye", ""]:
                break

            send_to, data = data.split(", ")

            # log names for localhost testing
            log.data_transfer([self.name, "server", send_to])
            log.data_transfer([self.name, "server", data])

            # do something
            for client in client_connections:
                if client.name == send_to:
                    self.conn.send("Found user\n".encode())

                    # found user is listening
                    client.conn.send(f"{data}\n".encode())
                    log.data_transfer(["server", client.name, data])

        log.info(f"{self.name} {self.addr} closed connection")
        self.conn.send("\n\nServer closing connection...".encode())
        self.conn.close()


class Server(object):
    global client_connections

    def __init__(self):
        self.server = None
        self.IP = None

        self.set_ip()
        self.run_server()

    # try to get LAN ip from router
    def set_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.254.254.254', 1))
        self.IP = s.getsockname()[0]
        s.close()

    def run_server(self):
        try:
            self.server_loop()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            pass

        self.end_all()

    def show_all_connections(self):
        for c in client_connections:
            print(c.name)

    def server_loop(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        log.info(f"Server with IP {self.IP} on port {PORT}...")

        self.server.listen(1000)
        log.info(f"Server listening for connections...")
        while True:
            conn, addr = self.server.accept()
            conn.send("login: ".encode())
            name = conn.recv(1024).decode().strip()

            log.info(f"{name} connected from {addr}.")

            new_client = Client(conn, addr, name)
            new_client.start()

            client_connections.append(new_client)
            self.show_all_connections()

    def end_all(self):
        self.server.close()


if __name__ == '__main__':
    s = Server()
