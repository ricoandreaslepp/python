# import uuid; uuid = str(uuid.uuid4()) # for future use
from logger import Log

class Client:

    def __init__(self, conn, addr):
        self.conn = conn
        self.client_loop(addr)

    def client_loop(self, addr):
        self.conn.send("Successfully connected to server...".encode())

        while True:
            self.conn.send("\nSay: ".encode())
            recv_data = self.conn.recv(1024).decode().strip()
            
            # do we care for how the connection was closed?
            if recv_data in ["bye", ""]:
                break

            Log.info(f"[data][{addr[0]}:{addr[1]} -> server] Received [{recv_data}]")

            # do something
            sent_data = recv_data[::-1]
            self.conn.send(sent_data.encode())
            Log.info(f"[data][server -> {addr[0]}:{addr[1]}] Sent [{sent_data}]")

        Log.info(f"Client {addr} closed connection")
        self.conn.send(b"\n\nServer closing connection...")
        self.conn.close()
