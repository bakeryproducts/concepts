# basic socket operations, works for HTTP, not HTTPS!
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

server = 'winrus.com'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = 'GET / HTTP/1.1\nHost: ' + server + '\n\n'
s.connect((server, port))
s.send(request.encode())
result = s.recv(1024)

while (len(result) > 0):
    print(result)
    result = s.recv(1024)
