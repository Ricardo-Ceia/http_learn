import socket
from http_utils.py import contains_special_characters,is_hex_char
"""HTTTP SERVER FOR JUST POST METHOD"""

host = '0.0.0.0'
port = 5013
s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

conn,addr = s.accept()

cont = True

while cont:
    try:
        data = conn.recv(1024)

        if not data:
            break
        cont = False 
        validate_http_request(data.decode())
    except socket.error as e:
        print(f"Error: {e}")
        break

conn.close()