import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))

server.listen()

client, addr = server.accept()

endcall = False

while not endcall:
    msg = client.recv(1024).decode('utf-8')
    if msg == "end call":
        endcall = True
    else:
        print(msg)
    client.send(input("Message: ").encode('utf-8'))
