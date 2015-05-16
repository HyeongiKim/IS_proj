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

def rsa(a,b):

def main():
	a = input("a: ");
	b = input("b: ");
	c = gcd(a, b);
	print("gcd : %d\n" % c)
	return;
main();
