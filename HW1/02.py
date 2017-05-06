a=input()
b=input()
print(hex(int(a, 16) ^ int(b, 16))[2:].zfill(len(a)))