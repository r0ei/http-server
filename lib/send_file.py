from socket import socket

def send_file(conn: socket, file: str, headers: list) -> None:
        conn.send(f'HTTP/1.1 {headers[0]}\nContent-Type: {headers[1]}\nDate: {headers[2]}\nContent-Length: {headers[4]}\nServer: {headers[3]}\n\n'.encode() + headers[5])