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

def validate_content_type_format(body,content_type):
    #from one list object to string
    body = body[0]
    if len(body)==0:
        return False
    if content_type == 'application/x-www-form-urlencoded':
        pairs = body.split('&')
        for pair in pairs:
            if not '=' in pair:
                return False
            key,value = pair.split('=')

            if not key:
                return False
    return True
              
   
def validate_http_request(request):
    lines = request.split('\r\n')
    method,uri,http_version = lines[0].split(' ')
    if method not in METHODS:
        return False

    headers = {}
    body_position = 0
    for i,line in enumerate(lines[1:]):
        if len(line)==0:  # Empty line indicates end of headers
            body_position = i+2
            break
        if len(line.split(":"))!=2:  # Must have header_name header_value -> pair
            return False
        header_name,header_value = line.split(':')
       
        for c in header_name:
            if not c.isalnum() and c!='-':
                return False 
        headers[header_name] = header_value.strip()

     
    if 'Content-Type' in headers and 'Content-Length' in headers:
        body = lines[body_position:]
        if not validate_content_type_format(body, headers['Content-Type']):
            return False
        
        if len((body[0])) != int(headers['Content-Length']):
            return False

    return True


valid_req = validate_http_request("POST /submit-form HTTP/1.1\nHost: www.example.com\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\nAccept: text/html,application/xhtml+xml\nAccept-Language: en-US,en;q=0.9\nAccept-Encoding: gzip, deflate\nConnection: keep-alive\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 50\nusername=john&password=secret&invalid_field=test")

print(f"THE REQ IS: {valid_req}")