from binascii import hexlify

def xor(str, key):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(str,(key*len(str))[:len(str)]))

char=input()
str=input()

print(hexlify(xor(str,char).encode()).decode())