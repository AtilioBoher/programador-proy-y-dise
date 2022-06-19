import serial
import time

# constants
fileName = "5_concatenado.hex"
comPort = "COM5"
baudRate = 115200

# this function sends data and print the response
def sendAndPrintResponse(serialObject, dataToSend):
    time.sleep(0.1)
    serialObject.write(dataToSend)

    time.sleep(0.1)
    thereIsDataLeft = True
    while thereIsDataLeft:
        received = serialObject.readline()   # se puede usar "serialObject.readline().decode('ascii')"
        print(received[:-1])            # pero a veces tira error y dice que no puede decodificar un valor
        if received == b'': thereIsDataLeft = False

# this function visualising if the data was successfully written
def checkData(serialObject, dataToSend, dataToCheck):
    aux = ""
    for i in range(1, len(dataToCheck), 2):
        aux = aux + dataToCheck[i-1:i+1] + " "
    print("           ", end="")
    print(aux)
    
    time.sleep(0.1)
    serialObject.write(dataToSend)

    time.sleep(0.1)
    thereIsDataLeft = True
    while thereIsDataLeft:
        received = serialObject.readline()   # se puede usar "serialObject.readline().decode('ascii')"
        print(received[:-1])            # pero a veces tira error y dice que no puede decodificar un valor
        if received == b'': thereIsDataLeft = False

#this part read the .hex file and extracts the necessary data
with open(fileName, "r") as f:
    lines = f. readlines()
    numOfBytes = []
    addr1 = []
    addr2 = []
    recordType = []
    data = []
    hexData = []
    for l in lines:
        numOfBytes.append(l[1:3])   # this we need as int
        addr1.append(l[3:7])                 # this one as hexadecimal
        addr2.append(numOfBytes[-1])
        if len(addr2[-1]) == 1:             # este bloque agrega ceros a addr2 para que tenga cuatro digitos
            addr2[-1] = "000" + addr2[-1]
        elif len(addr2[-1]) == 2:
            addr2[-1] = "00" + addr2[-1]
        elif len(addr2[-1]) == 3:
            addr2[-1] = "0" + addr2[-1]
        recordType.append(l[7:9])           # therre is no need to change this
        data.append(l[9:-3])                # read the data bytes
        hexData.append(l[9:-3])             # this is for checking after the writing process

    for i in range(len(data)):   # rearrange the data bytes conveniently as ints (one byte per element of the list)
        aux = data[i]
        data[i] = []
        for j in range(1,len(aux),2):
            data[i].append(int(aux[j-1:j+1],16))

# at this point all the data has been extracted and the file is automatically closed with the "with" statement
# now we create the instructions, there is one instruction per line of the .hex file, one instruction to write data,
# and another to read data. The latter will be use to check if the data was successfully written
writeInstr = []    # instruction
readInstr = []
for i in range(len(recordType)):
    if recordType[i] == "00":
        writeInstr.append(bytes("w," + addr1[i] + "," + addr2[i] + "," + numOfBytes[i], "ASCII") + bytes([10]) +
        bytes(data[i]) + bytes([10]))
        
        readInstr.append(bytes("R," + addr1[i] + "," + addr2[i], "ASCII") + bytes([10]))

# now the loading part starts
arduino = serial.Serial(
    port = comPort,
    baudrate = baudRate,
    timeout = 0.1)

time.sleep(3)   # por alguna razón el arduino se reinicia cuando se corre el programa,
                # por lo que hay que esperar a que se encienda
try:
    for i in range(len(recordType)):
        if recordType[i] == "00":
            sendAndPrintResponse(arduino, writeInstr[i])
    print("La escritura a finalizado \nA continuación se muestran los datos en la memoria \n")
    for i in range(len(recordType)):
        if recordType[i] == "00":
            checkData(arduino, readInstr[i], hexData[i])
finally:
    arduino.close()

print("the program finished its execution correctly")