# HW5	Shanks' algorithm
# ID	20110032
# Name	Kim Hyeongi

from math import sqrt

#Extended euclid algorithm
def egcd(a,b):
	if a==0:
		return (b,0,1)
	else:
		g,y,x = egcd(b%a,a)
		return (g,x - (b//a)*y,y)

# Calculate inverse modular
def inverse_mod(a,m):
	g,x,y = egcd(a,m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

# Find matching pair
def find_match(S, T):
	for j_pair in S:
		for i_pair in T:
			if j_pair[1] == i_pair[1]:
				return j_pair[0],i_pair[0]
	return -1,-1

# Shanks' baby-step giant-step algorithm
def shanks(p,a,b):
	# Initialization
	m = int(sqrt(p-1)//1 + 1)
	j_pair = int(pow(a,m)%p)
	
	J = []
	# Ordered pairs (j, pow(j_pair,j) mod p) for 0<=j<=m-1
	for j in range(29):
		pair = [j,pow(j_pair,j,p)]
		J.append(pair)
	
	I = []
	# Ordered pairs (i, b*pow(pow(a,i),-1)mod p) for 0<=i<=m-1
	for i in range(29):
		pair = [i,(b*inverse_mod(pow(a,i),p)%p)]
		I.append(pair)
	
	# Find match
	j,i = find_match(J, I)
	if (j,i) == (-1,-1):
		raise Exception('Fail to find match')
	
	ans = (m*j + i)%(p-1)
	#Confirmation
	if pow(a,ans,p) != b:
		raise Exception('Fail to confirm')
	return ans

# Print ans
def main():	
	p = 809
	a = 3
	b = 500
	print "p = %d,\nlog(%d)/log(%d)" %(p,b,a)
	ans = shanks(p,a,b)
	print "= ",ans,"(Ans)"
	return

main()
