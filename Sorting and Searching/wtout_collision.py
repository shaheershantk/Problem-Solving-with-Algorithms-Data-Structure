#hashing function without collision(string)
def wthout_col(data,table_size):
	sum = 0
	for pos in range(len(data)):
		sum = sum + (ord(data[pos])*(pos + 1))
	return sum % table_size

print wthout_col("cat",11)
