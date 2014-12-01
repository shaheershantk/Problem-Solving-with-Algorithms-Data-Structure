def pal(n):
	if n=="":
		return True
	elif ord(n[0])==ord(n[-1]):
		return pal(n[1:-1])
	else:
		return False
print pal("kayak")
print pal("malayalam")
print pal("hello")
print pal("kanakanak")
