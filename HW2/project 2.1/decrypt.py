from oracle import *
import sys

if len(sys.argv) < 2:
	print "Usage: python decrypt.py <filename>"
	sys.exit(-1)

f = open(sys.argv[1])
data = f.read()
f.close()

data = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]

block = 16
mesLenByte=len(data) #48

def paddingUpdate(ctext, padding):
	for i in range(1,padding):
		ctext[-i]=ctext[-i]^(padding-1)^padding
	ctext[-padding]=ctext[-padding]^padding	

def decryptBlock(iv, ctext, currPadding):
	ans=""
	for h in range(currPadding+1,17):
		paddingUpdate(iv,h)
		save=iv[-h]
		for i in range(256):
			iv[-h]=save^i
			if (Oracle_Send(iv+ctext,2)):
				ans=chr(i)+ans
				break
	return ans

def find_padding(i, iv, ctext):
	if Oracle_Send(iv+ctext,2):
		iv[i] += 1
		return find_padding(i+1, iv, ctext)
	else:
		return i-1

Oracle_Connect()
ans=""
p=block-find_padding(0, data[-2*block:-block], data[-block:])
for i in range(mesLenByte, block, -block):
	ans=decryptBlock(data[i-2*block:i-block], data[i-block:i], p)+ans
	p=0

print ans
Oracle_Disconnect()