from http import server
import socket

server.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname
port = 444
serversocket.bind(host, port)
serversocket.listen(3)
while True:
  clientsocket, address = serversocket.accept()
  print ("received connection from " % str(address))

  massage = "hello! Thank you for contacting to the server" + "\r\n"
  clientsocket.send(massage)
  clientsocket.close()
