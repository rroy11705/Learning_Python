import socket

localIP = '127.0.0.1'
localPORT = 20001

bufferSize = 1024

magFromServer = "Hello UPD Client"

bytesToSend = str.encode(magFromServer)

UPD_SERVER_SOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UPD_SERVER_SOCKET.bind((localIP, localPORT))

print("UDP server connected")

while True:
    bytesAddressPair = UPD_SERVER_SOCKET.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)

    print(clientMsg)
    print(clientIP)

    UPD_SERVER_SOCKET.sendto(bytesToSend, address)
