def is_even(k):
	n = '{:0b}'.format(k) 
	if n[-1] == '1':
		return False
	else:
		return True

#-----Driver Function-----

k = int(input())
print(is_even(k))


"""
Explaination: Convert the no into the binary format and check the last
element of the output if it's 1 then its an odd no but if it's 0 then
it's even

"""
