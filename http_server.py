import socket
"""HTTTP SERVER FOR JUST POST METHOD"""

#INCOMPLETE
def url_encodeed_parser_verifier(data):
    splited_data = data.split("=")
    print(f"splited_Data:{splited_data}")
        
#INCOMPLETE
def validate_http_request(request):
    lines = request.split('\r\n')
    print("Test:",lines[1])
    if len(lines)<1:
        return False


    headers = {}
    print(f"test:{lines[1:]}")
    host = lines[1]
    content_type = lines[2]
    content_length = lines[3]
    print(f"host:{host} content_type:{content_type} content_length:{content_length}")

    body = lines[5]

    if len(body) != int(content_length.split(':')[1]):
        return False 
    validate_http_request(body)


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