bla=[0,0,0,0,0,0,0,0,0,0,0,5,4,3,2,1]
from oracle import *
import sys

print bla[-4:]
print bla[-8:-4]

a=7
b="s"

print(str(a)+b)

def paddingUpdate(ctext, padding):
	for i in range(1,padding):
		ctext[-i]=ctext[-i]^(padding-1)^padding
	ctext[-padding]=ctext[-padding]^padding	

def decryptBlock(iv, ctext, currPadding):
	ans=""
	for h in range(currPadding+1,17):
		#print (h,ans)
		paddingUpdate(iv,h)
		save=iv[-h]
		for i in range(256):
			#print iv
			iv[-h]=save^i
			#print iv+ctext
			if (Oracle_Send(iv+ctext,2)):
				ans=chr(i)+ans
				break
	return ans





Oracle_Connect()

iv=[159, 11, 19, 148, 72, 65, 168, 50, 178, 66, 27, 158, 175, 109, 152, 54]
ctext=[129, 62, 201, 217, 68, 165, 200, 52, 122, 124, 166, 154, 163, 77, 141, 192]
print(decryptBlock(iv,ctext,0))

Oracle_Disconnect()