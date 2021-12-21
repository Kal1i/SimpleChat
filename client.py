import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("localhost",9999))

endcall = False

while not endcall:
    client.send(input("Message: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == "end call":
        endcall = True
    else:
        print(msg)
