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
	for i in range(4):
		if(((bit>>i)&1) == 1):
			count+=1
	return count;

# num -> S5(num)
def sbox_prop(num):
	table =[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
			[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
			[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
			[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
	
	row = ((num>>5)&1)*2+((num&1));
	column = ((num&30)>>1);

	return table[row][column];

# Check all cases about 0~63
def check_bit():
	for i in range(64):
		bit = sbox_prop(i)^sbox_prop(i^12)
		print "x ",
		binary_trans(i,5)
		print " S5(x) ",
		binary_trans(sbox_prop(i),3)
		print " S5(xor) ",
		binary_trans(sbox_prop(i^12),3)
		print " diff_bits %d" % bitcount(bit)
	return;	
check_bit();
