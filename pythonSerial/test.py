data = bytearray(b'w,0000,0002,02')
program = bytearray([10, 122, 248, 10])
print(type(program))
for p in program:
    data.append(p)

print("datos: ", data, "\nlenght of data: ", len(data), "\n")