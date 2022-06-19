import serial
import time

arduino = serial.Serial(
    port = "COM6",
    baudrate = 115200,
    timeout = 0.1)

time.sleep(3)   # por alguna razón el arduino se reinicia cuando se corre el programa,
                # por lo que hay que esperar a que se encienda

""" aux = []    # inicio un arreglo con enteros del 0 al 255
for i in range(256):
    aux.append(i) """

# el arreglo es muy grande como para enviarlo todo de una, de a 50 bytes sí recibe bien todos los datos
# o lo puedo iterar en el for también

""" data = bytes(aux) # como valores decimales """
""" data = b'R,0000,000D\n' # como un string """
data = b'w,0000,000D,0D' + bytes([10, 0x7A, 0xF8, 0x10, 0xB1, 0x21, 0x91, 0x3A, 0x04, 0x31, 0x00, 0x7B, 0x30, 0x01, 10])
print("datos: ", data, "\nlenght of data: ", len(data), "\n")

arduino.write(data)
time.sleep(0.1)

thereIsDataLeft = True
while thereIsDataLeft:
    received = arduino.readline()   # se puede usar "arduino.readline().decode('ascii')"
    print(received[:-1])            # pero a veces tira error y dice que no puede decodificar un valor
    if received == b'': thereIsDataLeft = False 


arduino.close()