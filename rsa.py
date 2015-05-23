######################
## HW4 	RSA			##
## ID   20110032    ##
## Name Kim Hyeongi ##
######################

def gcd(a,b):
	while (b!=0):
		temp = a%b
		a = b
		b = temp
	return a

def extended_euclid(d,f):
	x_1 = 1
	x_2 = 0
	x_3 = f
	y_1 = 0
	y_2 = 1
	y_3 = d
	while (y_3 != 1):
		if(y_3 == 0):	# No inverse
			return -1
		q = x_3/y_3
		t_1 = x_1 - q*y_1
		t_2 = x_2 - q*y_2
		t_3 = x_3 - q*y_3

		x_1 = y_1
		x_2 = y_2
		x_3 = y_3
		y_1 = t_1
		y_2 = t_2
		y_3 = t_3

	return y_2  		# d^-1 mod f
	
	
def find_e(pi_n):
	e = 2
	while(gcd(e,pi_n)!=1):
		e+=1
	return e


def rsa(p, q, m):
	#Key Generation
	print "-"*30
	print "p = %d\nq = %d\nM = %d\n" % (p,q,m)
	print "<Key Generation>"
	
	n = long(p*q)
	pi_n = (p-1)*(q-1)
	e = long(find_e(pi_n))
	d = long(extended_euclid(e,pi_n))
	
	print ("n: %d\npi_n: %d\ne: %d\nd: %d" % (n, pi_n, e, d))
	
	#Encryption
	C = pow(m,e) % n

	#Decryption
	M = pow(C,d) % n
	
	print "\n<Encryption & Decryption>"
	print ("Ciphertext C	: %d\nPlaintxt M	: %d" % (C, M))
	print "-"*30
	return

def main():
	rsa(3,11,5)
	rsa(2357,2551,1234)
	rsa(885320963,238855417,1234567)
	return
main()
