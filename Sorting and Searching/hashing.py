def hash_str(string,table_size):
	sum = 0
	for pos in range(0,len(string)):
		sum = sum + ord(string[pos])
	return sum % table_size
print hash_str("cat",11)
