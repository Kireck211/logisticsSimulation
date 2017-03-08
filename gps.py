import socket
import datetime
from random import randint
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
f = open("locations.txt", "r")
locations = []

def calcCoordValue (val, is_lon):
    aval = abs(val)
    grad = int(aval)
    minu = (aval - grad) * 60.0
    coordenada = str(grad) + str(minu) + ";"
    if (is_lon):
        if (val <0):
            coordenada = coordenada + "W"
        else:
            coordenada = coordenada + "E"
    else:
        if (val < 0):
            coordenada = coordenada + "S"
        else:
            coordenada = coordenada + "N"
    return coordenada

def initialization():
	global clientsocket
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('193.193.165.165', 20332))
	clientsocket.send('#L#123456789321;12345\r\n'.encode())
	data = clientsocket.recv(1024)
	print ("Received response:" + str(data))

def converter (lat, longi,speed):
	primera_parte = calcCoordValue(lat, False)
	segunda_parte = calcCoordValue(longi, True)
	utc_datetime = datetime.datetime.utcnow()

	mensaje = "#SD#" + utc_datetime.strftime("%d%m%y") + ";" + utc_datetime.strftime("%H%M%S")+ ";" + primera_parte + ";" + segunda_parte + ";" + str(speed) + ";0;300;7" 
	return mensaje

def send(latitude, longitude,speed):
	global clientsocket
	clientsocket.send("{}\r\n".format(converter(latitude, longitude,speed)).encode())
	data = clientsocket.recv(1024)
	print("Received response: " + str(data))

def run():
	global locations
	deliveries = int(f.readline())
	for i in range(0, deliveries):
		locations.append(str(f.readline()).split(','))



f.close()