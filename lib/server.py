from socket import socket, AF_INET, SOCK_STREAM, SHUT_WR, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from . import recv_get, send_file, extract_file, headers
from os import getcwd, path
from termcolor import colored

class HttpServer:
    def __init__(self):
        sock = socket(AF_INET, SOCK_STREAM) # IPv4, TCP

        self.bind_socket(sock) # bind socket to ip and port
        self.accept_clients(sock) # Start accept 10 clients

    def on_new_client(self, client: socket) -> None:
        while True:
            if not (req := recv_get.recv_requests(client)):
                break
            if path.isdir(file_name := extract_file.extract_file(req)):
                send_file.send_file(client, getcwd() + '/html/index.html', headers.response_headers(getcwd() + '/html/index.html')); continue
            send_file.send_file(client, file_name, headers.response_headers(file_name))

    def __repr__(self) -> str:
        return 'Made by r0eilevi \u2661'

    def accept_clients(self, socket: socket) -> None:
        for _ in range(11):
            conn, _ = socket.accept()
            Thread(target=self.on_new_client, args=(conn,)).start()

    def bind_socket(self, socket: socket) -> None:
        socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        socket.bind(('0.0.0.0', 14143))
        socket.listen(10) # 10 clients max

        print(colored(f'Serving at http://localhost:14143', 'green'))