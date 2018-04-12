def square_odd(n):
	sum = 0
	for i in range(1,n+1):
		if i%2!=0:
			sum += i*i
	return sum

#-----Driver Function-----

t = int(input())
print(square_odd(t))