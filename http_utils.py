import sys

METHODS = ["POST","GET","HEAD","PUT","DELETE"]

def contains_special_characters(data):
    special_characters = set('@&+/:;=?\"<>#%{}|\\^~[]`()')
    return len(set(data) & special_characters)> 0 #return True if the intersection of sets its not empty


def is_hex_char(char):
    return char in '0123456789ABCDEFabcdef'

def url_encoded_parser_verifier(data):
    if contains_special_characters(data):
        return False
    
    for i,c in enumerate(data):
        if c=='%':
            if i+2<len(data):
                if not is_hex_char(data[i+1]) and is_hex_char(data[i+2]):
                    return False

    return True

#TODO
def validate_content_type_format(body,content_type):
    pass
#IMCOMPLETE    
def validate_http_request(request):
    lines = request.split('\r\n')
    method,uri,http_version = lines[0].split(' ')
    if method not in METHODS:
        return False

    headers = {}
    body_position = 0
    for i,line in enumerate(lines[1:]):
        if not len(line)==0:#Remove empty line
        body_position = i+1
            break
            if len(line.split(":"))!=2:#Most have header_name header_value -> pair
                return False
            header_name,header_value = line.split(':')
            for c in header_name:
                if not c.isalphanum() or c=='-':
                    return False 
            headers[header_name] = header_value.strip()
    
    if headers['Content-Type'] and headers['Content-Length']:
        body = lines[body_position:]
        if not validate_content_type_format(lines[body_position:],headers['Content-Type']):
            return False

        
        if sys.getsizeof(body)!=headers['Content-Length']:
            return False

    return True




validate_http_request("GET /index.html HTTP/1.1\r\nHost: www.example.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\nAccept: text/html,application/xhtml+xml\r\nAccept-Language: en-US,en;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n")