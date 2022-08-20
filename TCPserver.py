from http import server
import socket

#creating the socket object
server.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = 192.168.0.103
host = socket.gethostbyname
port = 444

#Binding to socket
serversocket.bind('192.168.0.103', port)#host will be replaced|substituted with IP changed and not running on host

#starting TCP listener
serversocket.listen(3)

while True:
  #starting the connection
  clientsocket, address = serversocket.accept()
  print ("received connection from %s" % str(address))

  massage = "hello! Thank you for contacting to the server" + "\r\n"
  clientsocket.send(massage.encode('ascii'))
  clientsocket.close()
