import serial
import time

arduino = serial.Serial(
    port = "COM6",
    baudrate = 115200,
    timeout = 0.1)

time.sleep(3)   # por alguna razón el arduino se reinicia cuando se corre el programa,
                # por lo que hay que esperar a que se encienda

aux = []    # inicio un arreglo con enteros del 0 al 255
for i in range(256):
    aux.append(i)

# el arreglo es muy grande como para enviarlo todo de una, de a 50 bytes sí recibe bien todos los datos
# o lo puedo iterar en el for también

data = bytes(aux) # como valores decimales
# data = b'atilio boher' # como un string
print("datos: ", data, "\nlenght of data: ", len(data), "\n")


for i in range(len(data)):
    arduino.write([data[i]]) # arduino.write() recibe una lista, [data[i]] es una lista de un elemento, que es del tipo byte
    # time.sleep(0.1)    # al parecer no hace falta esperar,
    received = arduino.readline()   # se puede usar "arduino.readline().decode('ascii')"
    print(received[:-1])            # pero a veces tira error y dice que no puede decodificar un valor

arduino.close()