from socket import socket

def recv_requests(conn: socket) -> str:
        return conn.recv(1024).decode() # HTTP request