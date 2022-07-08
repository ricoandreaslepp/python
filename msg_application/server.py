from config import HOST, PORT
import socket
from _thread import *
from server_side_client import Client
from logger import Log
# import threading # for thread locking

class Server:

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
        Log.info(f"Server with IP {self.IP} on port {PORT}...")

        self.server.listen(1000)
        Log.info(f"Server listening for connections...")
        while True:
            conn, addr = self.server.accept()
            Log.info(f"Got connection from {addr}.")

            start_new_thread(Client, (conn, addr,))

    def endall(self):
        self.server.close()

if __name__=='__main__':
    s = Server()