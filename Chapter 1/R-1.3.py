# Method 1
def minmax(data):
	min_value = max_value = data[0]
	l = len(data)
	for i in range(l):
		if max_value < data[i]:
			max_value = data[i]

		if min_value > data[i]:
			min_value = data[i]

	return max_value,min_value

"""# Method 2
def minmax_2(data):
	data = sorted(data)
	max_value = data[-1]
	min_value = data[0]
	return max_value,min_value"""

#---------Driver function-------
t = list(map(int,input().split()))
print(minmax(t))
print(minmax_2(t))