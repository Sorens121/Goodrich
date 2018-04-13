def reverse(arr):
	x = []
	for i in range(len(arr)):
		x.append(arr[-(i+1)])
	return x

#-----Driver Function------

arr = list(map(int,input().split()))
print(reverse(arr))