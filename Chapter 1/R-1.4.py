#-----Method 1-----
def square(t):
	n = t-1
	sum = (n*(n+1)*(2*n+1))//6
	return sum
#-----Method 2------
"""def square2(t):
	sum = 0
	i = 1
	while t>i:
		sum +=i*i
		i+=1
	return sum"""

#------Driver Function------
t = int(input())
print(square(t))
#print(square2(t))