from oracle import *
import sys

if len(sys.argv) < 2:
	print "Usage: python sample.py <filename>"
	sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

block=16
mesLenBytes=len(data)

def xor(a, b):
	res=bytearray(len(a))
	for x in range(len(a)):
		res[x]=a[x] ^ b[x]
	return res

Oracle_Connect()

# first tag
mes=data[0:2*block]
tag = Mac(mes, len(mes))

# update tag for each two blocks
for i in range(2*block, mesLenBytes, 2*block):
	mes1=xor(tag,bytearray(data[i:i+block]))
	mes2=data[i+block:i+2*block]
	mes=mes1+mes2
	tag = Mac(mes, len(mes))


ret = Vrfy(data, len(data), tag)

if ret == 1:
	print "Message verified successfully!"
else:
	print "Message verification failed."

Oracle_Disconnect()
