# import uuid; uuid = str(uuid.uuid4()) # for future use
# import threading # for thread locking

from config import HOST, PORT
import socket
from _thread import *
from logger import log

class Client(object):

    def __init__(self, conn, addr):
        self.conn = conn
        self.client_loop(addr)

    def client_loop(self, addr):
        self.conn.send("Successfully connected to server...".encode())

        while True:
            recv_data = self.conn.recv(1024).decode().strip()
            
            # do we care for how the connection was closed?
            if recv_data in ["bye", ""]:
                break

            log.data_transfer([addr[0], "server", recv_data])

            # do something
            sent_data = recv_data[::-1]
            self.conn.send(sent_data.encode())
            log.data_transfer(["server", addr[0], sent_data])

        log.info(f"Client {addr} closed connection")
        self.conn.send(b"\n\nServer closing connection...")
        self.conn.close()

class Server(object):

    client_connections = []

    def __init__(self):
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

        self.endall()

    def server_loop(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        log.info(f"Server with IP {self.IP} on port {PORT}...")

        self.server.listen(1000)
        log.info(f"Server listening for connections...")
        while True:
            conn, addr = self.server.accept()
            log.info(f"Got connection from {addr}.")

            start_new_thread(Client, (conn, addr,))

    def endall(self):
        self.server.close()

if __name__=='__main__':
    s = Server()