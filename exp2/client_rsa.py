import socket
from Crypto.PublicKey import RSA

server = socket.socket()
host = "172.25.1.7"
port = 7777

server.connect((host, port))

#Tell server that connection is OK
output = "Client: OK"
server.sendall("Client: OK")

#Receive public key string from server
server_string = server.recv(1024)

#Remove extra characters
server_string = server_string.replace("public_key=", '')
server_string = server_string.replace("\r\n", '')

#Convert string to key
server_public_key = RSA.importKey(server_string)
print("Public Key from server: " + str(server_public_key))

#Encrypt message and send to server
message = "hello"
encrypted = server_public_key.encrypt(message, 32)
print("Message: " + message + "\n")
print("Encrpted Message: " + str(encrypted) + "\n")
server.sendall("encrypted_message="+str(encrypted))
print("Encryped message sent to server")
#Server's response
server_response = server.recv(1024)
server_response = server_response.replace("\r\n", '')
if server_response == "Server: OK":
    print ("Server decrypted message successfully")

#Tell server to finish connection
server.sendall("Quit")
print(server.recv(1024)) #Quit server response
server.close()
