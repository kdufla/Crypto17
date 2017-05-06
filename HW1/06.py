import binascii

def xor(str, key):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(str,(key*len(str))[:len(str)]))

FREQUENCY_TABLE = {'a': 0.0651738, 'b':0.0124248, 'c':0.0217339, 'd':0.0349835, 'e':0.1041442, 'f':0.0197881, 'g':0.0158610, 'h':0.0492888,
 'i':0.0558094, 'j':0.0009033, 'k':0.0050529, 'l':0.0331490, 'm':0.0202124, 'n':0.0564513, 'o':0.0596302, 'p':0.0137645, 'q':0.0008606, 
 'r':0.0497563, 's':0.0515760, 't':0.0729357, 'u':0.0225134, 'v':0.0082903, 'w':0.0171272, 'x':0.0013692, 'y':0.0145984, 'z':0.0007836, ' ':0.1918182}

def score(xored):
  sum=0
  for c in xored:
    try:
      sum=sum+FREQUENCY_TABLE[c]
    except KeyError as e:
      pass
  return sum

def breakCesar(str):
	scores={}
	for x in range(256):
		scores[x]=score(xor(str,chr(x)))
	maxx=max(scores, key=scores.get)
	return (xor(str,chr(maxx)))

def hamW(s):
	return sum([bin(s[i]).count('1') for i in range(len(s))])

def hamD(s1, s2):
	return hamW(xor(s1,s2).encode())

def transpose(list):
	l=[]
	st=''
	for i in range(len(list[0])):
		for o in list:
			try:
				st+=o[i]	
			except Exception as e:
				pass	
		l.append(st)
		st=''
	return l

def splitBlocks(message, keySize):
	return [message[i:i+keySize] for i in range(0, len(message), keySize)]

def breakMessage(b64,keySize):
	messages=[]
	message=binascii.a2b_base64(b64.encode()).decode()
	for m in transpose(splitBlocks(message,keySize)):
		messages.append(breakCesar(m))
	return ''.join(transpose(messages))

def keySize(b64):
	message=binascii.a2b_base64(b64.encode()).decode()
	avgs={}
	for size in range(2,40):
		l=[]
		for i in range(int((len(message)/size))-1):
			l.append(hamD(message[i*size:(i+1)*size],message[(i+1)*size:size*(i+2)])/size)
		avgs[size]=sum(l)/len(l)
	m=min(avgs, key=avgs.get)
	return m

def BreakRepeatingReyXOR(inp):
	return breakMessage(inp,keySize(inp))

print(BreakRepeatingReyXOR(input()))