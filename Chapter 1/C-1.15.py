#------Method 1-----

def is_unique(s):
	n = len(s)
	count = 0
	for i in range(1,n):
		for j in range(0,i):
			if s[j]==s[i]:
				count+=1
	if count == 0:
		return True
	else:
		return False
	#return count

#-----Method 2-----

def is_unique2(s):
	len_list = len(s)
	len_set = len(set(s))
	if len_list == len_set:
		return True
	else:
		return False

#----Driver Function----

arr = list(map(int,input().split()))
print(is_unique(arr))
print(is_unique2(arr))