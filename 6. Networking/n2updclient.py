import socket


msgFromClient = "hello udp server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ('127.0.0.1', 20001)

bufferSize = 1024

UPD_CLIENT_SOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UPD_CLIENT_SOCKET.sendto(bytesToSend, serverAddressPort)

msgFromServer = UPD_CLIENT_SOCKET.recvfrom(bufferSize)

msg = "message from server: {}".format(msgFromServer[0])

print(msg)
