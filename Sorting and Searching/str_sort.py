def str_sort(string):
	for pass_num in range(len(string) - 1, 0, -1):
		for i in range(pass_num):
			if ord(string[i]) > ord(string[i + 1]):
				temp = string[i]
				string[i] = string[i + 1]
				string[i + 1] = temp
string = ['P','Y','T','H','O','N']
str_sort(string)
print(string)
