import serial
import time

arduino = serial.Serial(
    port = "COM6",
    baudrate = 9600,
    timeout = 0.5)

time.sleep(3)
data = bytes([97, 116, 105, 108, 105, 111]) # como valores decimales
# data = b'atilio boher' # como un string
print("datos: ", data, "\nlenght of data: ", len(data))
arduino.write(data)

for x in range(len(data)):
    time.sleep(0.1)
    received = arduino.readline().decode('ascii')
    print(received[:-1])

arduino.close()