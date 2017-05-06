import binascii

def xor(str, key):
  return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(str,(key*len(str))[:len(str)]))

FREQUENCY_TABLE = {'a': 0.0651738, 'b':0.0124248, 'c':0.0217339, 'd':0.0349835, 'e':0.1041442, 'f':0.0197881, 'g':0.0158610, 'h':0.0492888,
 'i':0.0558094, 'j':0.0009033, 'k':0.0050529, 'l':0.0331490, 'm':0.0202124, 'n':0.0564513, 'o':0.0596302, 'p':0.0137645, 'q':0.0008606, 
 'r':0.0497563, 's':0.0515760, 't':0.0729357, 'u':0.0225134, 'v':0.0082903, 'w':0.0171272, 'x':0.0013692, 'y':0.0145984, 'z':0.0007836, ' ':0.1918182}

def score(xored):
  sum=0
  for c in xored.lower():
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


def bestMessage():
  n=int(input())
  messages=[]
  for x in range(n):
    try:
      messages.append(breakCesar(binascii.a2b_hex(input()).decode())) 
    except Exception as e:
      pass
  return max(messages, key=score)

print(bestMessage())