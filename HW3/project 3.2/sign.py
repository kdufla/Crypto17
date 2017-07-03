from oracle import *
from helper import *

# start stackoverflow
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
# end stackoverflow

def main():
	n = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869

	e = 65537

	Oracle_Connect()

	msg = "Crypto is hard --- even schemes that look complex can be broken"

	m = ascii_to_int(msg)

	s0=Sign(1)
	s1=Sign(2)
	s2=Sign(m/2)

	sigma = (s1 * s2 * modinv(s0, n)) % n
	assert(sigma < 0)

	if Verify(m, sigma):
		print "found"
		print hex(sigma)
	else:
		print "not found"	

	Oracle_Disconnect()

if __name__ == '__main__':
	main()