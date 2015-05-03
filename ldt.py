######################
## ID	20110032	##
## Name	Kim Hyeongi	##
######################

# Decimal number -> Binary number
def binary_trans(a,n):
	for i in range(n,-1,-1):
		if(i>=0):
			print("%d" % ((a>>i)&1)),
	return;

# Bit -> count how many different bits in 'bit'
def bitcount(bit):
	count = 0
	for i in range(6):
		if(((bit>>i)&1) == 1):
			count+=1
	return count;
# Parity check.
def parity(bit):
	sum_bit = 0
	for i in range(6):
		sum_bit += (bit>>i)&1
	ans = sum_bit%2
	return ans;
# num -> S5(num)
def sbox(num):
	table =[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
			[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
			[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
			[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
	
	row = ((num>>5)&1)*2+((num&1));
	column = ((num&30)>>1);

	return table[row][column];
# a,b -> NS5(a,b), NS5(a,b) = #{x|0<=x<64, parity(x&a)=parity(S(x)*b)};
def ldt(a,b):
	count = 0
	for x in range(64):
		if (parity(x&a) == parity(sbox(x)&b)):
			count+=1
	return count;
# Check all cases about 0~63
def check_bit():
	print ldt(16,15)
#		print (" x*a "),
#		binary_trans(i&16,6)
#		print (" S(x)*b "),
#		binary_trans(sbox_prop(i)&15,6)
#		print "\n"
	return
check_bit();
