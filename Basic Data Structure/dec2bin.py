from stack import Stack # As previously defined

def divide_by_2(dec_number):
	s = Stack()

	while dec_number > 0:
		rem = dec_number % 2
		s.push(rem)
		dec_number = dec_number // 2

	bin_string = ""
	while not s.is_empty():
		bin_string = bin_string + str(s.pop())

	return bin_string

print(divide_by_2(42))
